#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
import glob
import codecs
from scrapy.selector import Selector
import common


def profile(table, category):
    item = {}
    trs = table.xpath('TR')
    cells = [tr.xpath('TD/P/text()').extract() for tr in trs]
    item['category'] = category
    item['name'] = cells[0][1].rstrip()
    item['department'] = cells[0][3].rstrip()
    item['title'] = cells[0][5].rstrip()
    item['report_at'] = common.ROC2AD(cells[2][1])
    item['report_type'] = cells[2][3].rstrip()
    item['spouse'] = cells[5][1].rstrip()
    return item

def rows(table, items, attr):
    trs = table.xpath('TR')
    for tr in trs:
        if tr.xpath('TD/P/text()').re(u'本欄空白'):
            continue
        tds = [td.rstrip() for td in tr.xpath('TD/P/text()').extract()]
        items.append(dict(zip(attr['columns'], tds)))
    return items

models = json.load(open('models.json'))
files = [codecs.open(f, 'r', encoding='utf-8') for f in glob.glob('../data/xml/*.xml')]
for f in files:
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    x = Selector(text=f.read(), type='xml')
    tables = x.xpath('//Part/Sect/Table')
    model = {}
    items = []
    for table in tables:
        p = re.sub('\s', '', table.xpath('preceding-sibling::P[1]/text()').extract()[0])
        if re.search(u'公職人員', p):
            model = models.get(p, {})
            item = {}
            if model:
                item = {'meta': profile(table, p)}
        for category, attr in model.items():
            if re.search(category, p) and attr.get('name'):
                item.update({attr['name']: rows(table, item.get(attr['name'], []), attr)})
        if re.search(u'備註', p):
            for category, attr in model.items():
                if item.get(attr.get('name')):
                    del item[attr['name']][0]
            if item:
                items.append(item)
            item, model = {}, {}
    dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
    common.write_file(dump_data, '../data/json/pretty_format/%s.json' % fileName)
    dump_data = json.dumps(items)
    common.write_file(dump_data, '../data/json/%s.json' % fileName)
