#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
import glob
import codecs
import unicodedata
from scrapy.selector import Selector
import common


def profile(table, i):
    item = {}
    item['file_id'] = i
    cells = table.xpath('TR/TD/text()').extract()
    for i in range(0, len(cells), 2):
        try:
            if re.search(u'申報人姓名', re.sub('\s', '', cells[i])):
                name = re.sub(u'\s', '', cells[i+1])
                item['name'] = name
                if name.find(u'服務機關'):
                    item['name'] = re.sub(u'服務機關.*', '', name)
            if re.search(u'服務機關', re.sub('\s', '', cells[i])):
                item['department'] = re.sub('[a-zA-Z\s\d.]', '', cells[i+1])
            if re.search(u'職稱', re.sub('\s', '', cells[i])):
                item['title'] = re.sub('[a-zA-Z\s\d.]', '', cells[i+1])
            if re.search(u'申報日', re.sub('\s', '', cells[i])):
                item['report_at'] = common.ROC2AD(re.sub('\s', '', cells[i+1]))
            if re.search(u'申報類別', re.sub('\s', '', cells[i])):
                item['report_type'] = re.sub('\s', '', cells[i+1])
            if re.search(u'配偶', re.sub('\s', '', cells[i])):
                item['spouse'] = re.sub('\s', '', cells[i+1])
        except:
            print table
    return item

items = []
for i in range(1, 17428):
    if not os.path.exists('../../data/xml/no_meta/%s.xml' % i):
        continue
    f = codecs.open('../../data/xml/no_meta/%s.xml' % i, 'r', encoding='utf-8')
    print f.name
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    xml_text = unicodedata.normalize('NFC', f.read())
    xml_text = re.sub('<TH', '<TD', xml_text)
    xml_text = re.sub('</TH>', '</TD>', xml_text)
    x = Selector(text=xml_text, type='xml')
    table = x.xpath('//Table[1]')
    item = profile(table, i)
    items.append(item)
    f.close()
dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
common.write_file(dump_data, '../../data/json/pretty_format/no_meta_individual_info.json')
dump_data = json.dumps(items)
common.write_file(dump_data, '../../data/json/no_meta_individual_info.json')
