#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
import db_settings


reports = json.load(open('../data/json/property_individual.json'))
for report in reports:
    if report.get('file_id'):
        if os.path.exists('../../../individual/%s.pdf' % report['file_id']):
            os.rename('../../../individual/%s.pdf' % report['file_id'], '../../../pdf/individual/meta/%s_%s_%s_%s.pdf' % (report['file_id'], report['journal'], report['name'], report['category']))
