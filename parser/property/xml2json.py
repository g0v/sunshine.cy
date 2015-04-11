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


def profile(table, category):
    item = {}
    item['category'] = category
    cells = table.xpath('TR/TD/P/text()').extract()
    for i in range(0, len(cells), 2):
        if re.search(u'申報人姓名', re.sub('\s', '', cells[i])):
            item['name'] = re.sub('\s', '', cells[i+1])
        if re.search(u'服務機關', re.sub('\s', '', cells[i])):
            item['department'] = re.sub('[\s\d.]', '', cells[i+1])
        if re.search(u'職稱', re.sub('\s', '', cells[i])):
            item['title'] = re.sub('[\s\d.]', '', cells[i+1])
        if re.search(u'申報日', re.sub('\s', '', cells[i])):
            item['report_at'] = common.ROC2AD(re.sub('\s', '', cells[i+1]))
        if re.search(u'申報類別', re.sub('\s', '', cells[i])):
            item['report_type'] = re.sub('\s', '', cells[i+1])
        if re.search(u'配偶', re.sub('\s', '', cells[i])):
            item['spouse'] = re.sub('\s', '', cells[i+1])
    return item

def rows(table, items, attr):
    trs = table.xpath('TR')
    for tr in trs:
        if tr.xpath('TD/P/text()').re(u'(本欄空白|未達申報標準)') :
            return []
        tds = [''.join(td.xpath('P/text()').extract()).rstrip() for td in tr.xpath('TD')]
        if len([item for item in tds if item != '']) > (len(attr['columns'])-2):
            items.append(dict(zip(attr['columns'], tds)))
#       #--> 同一列的資料換頁被切開
#       elif tr == trs[0] and items:
#           pre_tds = items[-1]
#       #<--
    return items

models = json.load(open('models.json'))
files = [codecs.open(f, 'r', encoding='utf-8') for f in glob.glob('../../data/xml/*.xml')]
for f in files:
    print f.name
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    xml_text = unicodedata.normalize('NFC', f.read())
    x = Selector(text=xml_text, type='xml')
    tables = x.xpath('//Part/Sect/Table')
    model = {}
    items, item = [], {}
    for table in tables:
        pre_p = table.xpath('preceding-sibling::P[1]/text()').extract()
        if pre_p:
            p = re.sub('\s', '', pre_p[0])
        else:
            continue
        if re.search(u'^公職人員', p) or re.search(u'備註', p):
            if item.get('meta'):
                for category, rowdata in item.items():
                    if category != 'meta' and rowdata:
                        del rowdata[0]
                items.append(item)
            model = models.get(p, {})
            item = {}
            if model:
                item = {'meta': profile(table, p)}
        for category, attr in model.items():
            if re.search(category, p) and attr.get('name'):
                item.update({attr['name']: rows(table, item.get(attr['name'], []), attr)})
        if item.get('meta') and re.search(u'備註', p):
            item['meta'].update({'remark': ''.join(table.xpath('TR/TD/P/text()').extract())})
    dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
    common.write_file(dump_data, '../../data/json/pretty_format/%s.json' % fileName)
    dump_data = json.dumps(items)
    common.write_file(dump_data, '../../data/json/processed/%s.json' % fileName)
