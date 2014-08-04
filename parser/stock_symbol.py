#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import pandas as pd
import common
import db_settings


def stock():
    c.execute('''
        SELECT id, name
        FROM property_stock
    ''')
    return c.fetchall()

def update_symbol(symbol, id):
    c.execute('''
        UPDATE property_stock
        SET symbol = %s
        WHERE id = %s
    ''', (symbol, id))

def name2symbol(name):
    name = name.decode('utf-8')
    match = re.search(u'[(]', name)
    if match:
        name = name[:match.start()]
    df_e = df[df[u'簡稱'] == name]
    if not df_e.empty:
        return df_e.index[0]
    name = re.sub(u'金控$', u'金', name)
    name = re.sub(u'股份有限公司.*', '', name)
    df_e = df[df[u'簡稱'].str.contains(name) | df[u'全稱'].str.contains(name)]
    if not df_e.empty:
        return df_e.index[0]

conn = db_settings.con()
c = conn.cursor()
df = pd.read_excel(u'../data/xlsx/stock_symbol.xlsx', u'工作表1', index_col=0)
for id, name in stock():
    print id, name
    symbol = name2symbol(name)
    print symbol
    if symbol:
        update_symbol(str(symbol), id)
conn.commit()
