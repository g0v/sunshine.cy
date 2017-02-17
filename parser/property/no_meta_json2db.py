#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import db_settings


def upsert_reports(data):
    data.update({'download_url': 'http://sunshine.cy.gov.tw/GipOpenWeb/wSite/SpecialPublication/fileDownload.jsp?id=%s' % data['file_id']})
    c.execute('''
        SELECT id
        FROM reports_reports
        WHERE name = %(name)s AND file_id = ''
        ORDER BY journal_id
    ''', data)
    r = c.fetchone()
    if r:
        data.update({'id': r[0]})
        c.execute('''
            UPDATE reports_reports
            SET download_url = %(download_url)s, file_id = %(file_id)s
            WHERE id = %(id)s
        ''', data)
        return

conn = db_settings.con()
c = conn.cursor()

reports = json.load(open('../../data/json/no_meta_individual_info.json'))
for report in reports:
    break
    if not report.get('file_id') or not report.get('name'):
        continue
    upsert_reports(report)
conn.commit()


# Export auto-complete json file
import codecs
from pandas import *
from pandas.tools.merge import concat


df1 = read_sql("SELECT DISTINCT(name) as label, '人名' as category FROM reports_reports ORDER BY name", conn)
df2 = read_sql("SELECT DISTINCT(department) as label, '部會' as category FROM reports_reports ORDER BY department", conn)
df = concat([df1, df2])
f = codecs.open('../../website/cy/templates/common/search.json', 'w', encoding='utf-8')
f.write(df.to_json(orient='records'))
f.close()
