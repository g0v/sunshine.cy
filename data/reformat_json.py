#!/usr/bin/python
# -*- coding: utf-8 -*
import json
import codecs


def write_file(data, file_name):
    file = codecs.open(file_name, 'w', encoding='utf-8')
    file.write(data)
    file.close()

for file_name in ['property_individual.json', 'property_journal.json']:
    objs = json.load(open('json/%s' % file_name))
    dump_data = json.dumps(objs, sort_keys=True, indent=4, ensure_ascii=False)
    write_file(dump_data, 'json/pretty_format/%s' % file_name)
