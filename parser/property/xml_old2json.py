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
    cells = table.xpath('TR/TD/text()').extract()
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
    pre_tds = []
    for tr in trs:
        if tr.xpath('TD/text()').re(u'(本欄空白|未達申報標準)'):
            return []
        tds = tr.xpath('TD/text()').extract()
        if len(tds) < 2:
            pre_tds = tds
            continue
        columns = attr['columns']
        if pre_tds and (len(tds) + len(pre_tds)) == len(attr['columns']):
            pre_tds.extend(tds)
            tds = pre_tds
        if len(tds) < len(attr['columns']) and attr.get('columns_shortage') and attr['columns_shortage'].get(str(len(tds))):
            columns = attr['columns_shortage'][str(len(tds))]
        if len([item for item in tds if item != '']) > (len(columns)-2):
            items.append(dict(zip(columns, tds)))
        pre_tds = tds
#       #--> 同一列的資料換頁被切開
#       elif tr == trs[0] and items:
#           pre_tds = items[-1]
#       #<--
    return items

models = json.load(open('models.json'))
files = [codecs.open(f, 'r', encoding='utf-8') for f in glob.glob('../../data/xml/old/*.xml')]
for f in files:
    print f.name
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    xml_text = unicodedata.normalize('NFC', f.read())
    xml_text = re.sub('<TH', '<TD', xml_text)
    xml_text = re.sub('</TH>', '</TD>', xml_text)
    x = Selector(text=xml_text, type='xml')
    tables = x.xpath('//Div/Table')
    model = {}
    items, item = [], {}
    for table in tables:
        pre_p = table.xpath('preceding-sibling::P[1]/text()').extract()
        header = ''.join(table.xpath('TR[1]/TD/text()').extract())
        if pre_p:
            p = re.sub('\s', '', pre_p[0])
        else:
            continue
        if re.search(u'^公職人員', p) == None and re.search(u'^申報人姓名', header):
            p = u'公職人員財產申報表'
        if re.search(u'^公職人員', p):
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
            if re.search(u'^%s' % attr['columns_cht'], header) and attr.get('name'):
                item.update({attr['name']: rows(table, item.get(attr['name'], []), attr)})
        if item.get('meta') and re.search(u'備註', p):
            item['meta'].update({'remark': ''.join(table.xpath('TR/TD/P/text()').extract())})
    dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
    common.write_file(dump_data, '../../data/json/pretty_format/%s.json' % fileName)
    dump_data = json.dumps(items)
    common.write_file(dump_data, '../../data/json/%s.json' % fileName)
