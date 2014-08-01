#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
from os.path import expanduser
import db_settings



def insert_journals(data):
    c.execute('''
        INSERT INTO journals_journals(name, date)
        SELECT %(journal_id)s, %(date)s
        WHERE NOT EXISTS (SELECT 1 FROM journals_journals WHERE name = %(journal_id)s)
    ''', data)

def upsert_reports(data):
    for key in ['file_id']:
        data.update({key: data.get(key, '')})
    c.execute('''
        SELECT id
        FROM reports_reports
        WHERE journal_id = %(journal_id)s AND category = %(category)s AND name = %(name)s AND download_url is null
        ORDER BY id
    ''', data)
    r = c.fetchone()
    if r:
        data.update({'id': r[0]})
        c.execute('''
            UPDATE reports_reports
            SET download_url = %(download_url)s, at_page = %(at_page)s, file_id = %(file_id)s
            WHERE id = %(id)s
        ''', data)
        return
    c.execute('''
        INSERT INTO reports_reports(journal_id, category, name, department, title, download_url, at_page, file_id)
        SELECT %(journal_id)s, %(category)s, %(name)s, %(department)s, %(title)s, %(download_url)s, %(at_page)s, %(file_id)s
        WHERE NOT EXISTS (SELECT 1 FROM reports_reports WHERE journal_id = %(journal_id)s AND category = %(category)s AND name = %(name)s AND at_page = %(at_page)s) RETURNING id
    ''', data)

conn = db_settings.con()
c = conn.cursor()

reports = json.load(open('../data/json/property_individual.json'))
for report in reports:
#   if report.get('file_id'):
#       if os.path.exists(expanduser('~/pdf/individual/%s.pdf' % report['file_id'])):
#           os.rename(expanduser('~/pdf/individual/%s.pdf' % report['file_id']), expanduser('~/pdf/individual/meta/%s_%s_%s_%s.pdf' % (report['file_id'], report['journal'], report['name'], report['category'])))
    if report['category'] == u'01一般申報':
        report['category'] = u'公職人員財產申報表'
    elif report['category'] == u'04信託申報':
        report['category'] = u'公職人員信託財產申報表'
    else:
        continue
    report['department'], report['title'] = report['department'].split('/')
    journal_attr = report['journal'][:-1].split('(')
    report['journal_id'] = u'%s第%s期' % (journal_attr[1], journal_attr[0])
    insert_journals(report)
    upsert_reports(report)
conn.commit()
