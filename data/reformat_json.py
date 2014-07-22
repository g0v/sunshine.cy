#!/usr/bin/python
# -*- coding: utf-8 -*
import sys
sys.path.append('../../')
import json
import codecs
import common

for file_name in ['property_individual.json', 'property_journal.json']:
    objs = json.load(open('json/%s' % file_name))
    dump_data = json.dumps(objs, sort_keys=True, indent=4, ensure_ascii=False)
    common.write_file(dump_data, 'json/pretty_format/%s' % file_name)
