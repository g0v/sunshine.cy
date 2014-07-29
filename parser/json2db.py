#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
import glob
import codecs
import db_settings
import sql


conn = db_settings.con()
c = conn.cursor()

journals = json.load(open('../data/json/property_journal.json'))
sql.upsert_journals(c, journals)
conn.commit()

files = [open(f) for f in glob.glob('../data/json/*期.json')]
for f in files:
    reports = json.load(f)
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    for report in reports:
        if not report['meta'].get('report_at'):
            continue
        report['meta'].update({'journal_id': fileName})
        report_id, created = sql.upsert_reports(c, report['meta'])
#       if not created:
#           continue
        print report['meta']
        for category, dataset in report.items():
            if category == 'meta':
                continue
            if dataset:
                for data in dataset:
                    data.update({'report_id': report_id})
                getattr(sql, 'upsert_property_%s' % category)(c, dataset)
conn.commit()

# Export auto-complete json file
from pandas import *
import pandas.io.sql as psql
from pandas.tools.merge import concat


df1 = psql.frame_query("SELECT DISTINCT(name) as label, '人名' as category FROM reports_reports ORDER BY name", conn)
df2 = psql.frame_query("SELECT DISTINCT(department) as label, '部會' as category FROM reports_reports ORDER BY department", conn)
df = concat([df1, df2])
f = codecs.open('../website/cy/templates/common/search.json', 'w', encoding='utf-8')
f.write(df.to_json(orient='records'))
f.close()
