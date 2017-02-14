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
    cells = table.xpath('ancestor-or-self::p/following-sibling::table[1]/tr/td//text()').extract()
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

def rows(report, item):
    p_tags = report.xpath('ancestor-or-self::p/following-sibling::p[string-length(text()) > 0]')
    for p_tag in p_tags:
        p_text = p_tag.xpath('text()').extract_first().strip()
        for category, attr in model.items():
            rows = []
            if re.search(category, p_text):
                table = p_tag.xpath('following-sibling::table[1]')
                for tr in table.xpath('tr[position()>1]'):
                    if tr.xpath('td//text()').re(u'(本欄空白|未達申報標準)') :
                        break
                    tds, need_merge = [], []
                    for i, td in enumerate(tr.xpath('td'), 1):
                        td_text = re.sub('\s', '', td.xpath('string()').extract_first())
                        if tr.xpath('td[%d][not(contains(@style, "border-right-style:solid"))]' % i):
                            need_merge.append(td_text)
                            continue
                        if need_merge:
                            need_merge.append(td_text)
                            td_text = ''.join(need_merge)
                            need_merge = []
                        tds.append(td_text)
                    if len([td for td in tds if td != '']) > (len(attr['columns'])-2):
                        rows.append(dict(zip(attr['columns'], tds)))
                item.update({attr['name']: rows})
                break
        if item.get('meta') and p_tag.xpath(u'preceding-sibling::p[1][re:test(text(), "備\s*註")]'):
            item['meta'].update({'remark': p_text})
        if p_tag.xpath(u'following-sibling::p[1]/descendant-or-self::*[re:test(text(), "公\s*職\s*人\s*員.*表$")]'):
            break
    return item

models = json.load(open('models.json'))
files = [codecs.open(f, 'r', encoding='utf-8') for f in glob.glob(u'../../data/html/*.html')]
for f in files:
    print f.name
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    xml_text = unicodedata.normalize('NFC', f.read())
    x = Selector(text=xml_text, type='html')
    reports = x.xpath(u'//*[re:test(text(), "公\s*職\s*人\s*員.*表$")]')
    model = {}
    items = []
    for report in reports:
        pre_p = report.xpath('text()').extract()
        if pre_p:
            p = re.sub('\s', '', pre_p[0])
        else:
            continue
        model = models.get(p, {})
        item = {}
        if model:
            item = {'meta': profile(report, p)}
            items.append(rows(report, item))
    dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
    common.write_file(dump_data, '../../data/json/pretty_format/%s.json' % fileName)
    dump_data = json.dumps(items)
    common.write_file(dump_data, '../../data/json/processed/%s.json' % fileName)
