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


maps = dict(zip(['in_individual', 'in_profit', 'in_party', 'in_civil', 'in_anonymous', 'in_others', 'in_total', 'out_personnel', 'out_propagate', 'out_campaign_vehicle', 'out_campaign_office', 'out_rally', 'out_travel', 'out_miscellaneous', 'out_return', 'out_exchequer', 'out_public_relation', 'out_total', 'balance'], [u'個人捐贈收入', u'營利事業捐贈收入', u'政黨捐贈收入', u'人民團體捐贈收入', u'匿名捐贈收入', u'其他收入', u'收入合計', u'人事費用支出', u'宣傳支出', u'租用宣傳車輛支出', u'租用競選辦事處支出', u'集會支出', u'交通旅運支出', u'雜支支出', u'返還捐贈支出', u'繳庫支出', u'公共關係費用支出', u'支出合計', u'收支結存金額']))
files = [codecs.open(f, 'r', encoding='utf-8') for f in glob.glob('../../data/html/*.html')]
for f in files:
    print f.name
    fileName, fileExt = os.path.splitext(os.path.basename(f.name))
    xml_text = unicodedata.normalize('NFC', f.read())
    x = Selector(text=xml_text, type='html')
    reports = x.xpath(u'//*[contains(text(), "議員選舉") and not(@href)] | //*[contains(text(), "立法委員選舉") and not(@href)]')
    print('%d persons' % len(reports))
    model = {}
    items = []
    for report in reports:
        item = {}
        year_ROC = report.re(u'(\d+)\s*年')
        year = str(int(year_ROC[0])+1911)
        item['election_year'] = year
        report = report.xpath(u'ancestor-or-self::p')
        county = report.xpath(u'following-sibling::p[re:test(., "[縣市]$")]')
        item['county'] = county.xpath(u'text()').extract_first()
        if not item['county']:
            item['county'] = report.xpath(u'a[re:test(., "[縣市]$")]/text()').extract_first().split()[-1]
        item['name'] = report.xpath(u'following::*[re:test(., "政治獻金收支結算表")]/text()').extract_first().split()[0]
        if item['name'] == u'政治獻金收支結算表':
            item['name'] = county.xpath(u'following::a[@name]/text()').extract_first()
        item['name'] = re.sub(u'政治獻金收支結算表', u'', item['name'])
        item['name'] = re.sub(u'[。˙・•．.]', u'‧', item['name'])
        item['name'] = re.sub(u'[　\s()（）]', '', item['name'])
        item['name'] = item['name'].title()
        print 'county: "%s"' % item['county'], 'name: "%s"' % item['name']
        tds = [x.strip() for x in report.xpath('following-sibling::table[1]/tr/td/*/text()').extract()]
        for i in range(0, len(tds)):
            for key, value in maps.iteritems():
                if re.match(value, tds[i]):
                    item[key] = int(re.sub('[^-\d.]', '', tds[i+1]))
                    break
        items.append(item)

    # output json file
    if items:
        dump_data = json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False)
        common.write_file(dump_data, '../../data/json/pretty_format/political_contribution/%s.json' % fileName)
        dump_data = json.dumps(items)
        common.write_file(dump_data, '../../data/json/political_contribution/%s.json' % fileName)
