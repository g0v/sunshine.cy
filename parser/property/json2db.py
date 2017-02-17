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

journals = json.load(open('../../data/json/property_journal.json'))
for journal in journals:
    journal['download_url'] = journal['download_url'][0]
    sql.upsert_journals(c, journal)
conn.commit()

files = [open(f) for f in glob.glob('../../data/json/not_processed/*期.json')]
for f in files:
    reports = json.load(f)
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    for report in reports:
        try:
            if not report['meta'].get('report_at'):
                continue
            report['meta'].update({'journal_id': fileName})
            report_id, created = sql.upsert_reports(c, report['meta'])
            if not created:
                continue
            for category, dataset in report.items():
                if category == 'meta':
                    continue
                if dataset:
                    for data in dataset:
                        data.update({'report_id': report_id})
                    getattr(sql, 'upsert_property_%s' % category)(c, dataset)
        except:
            print fileName, fileExt
#           for k, v in report.items():
#               print k, v
            raise
conn.commit()
