#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
from os.path import expanduser
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

reports = json.load(open('../data/json/no_meta_individual_info.json'))
for report in reports:
    if not report.get('file_id') or not report.get('name'):
        continue
    upsert_reports(report)
conn.commit()
