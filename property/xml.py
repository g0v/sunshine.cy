#! /usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from scrapy.selector import Selector


f = codecs.open('data/xml/f66.xml', 'r', encoding='utf-8')
x = Selector(text=f.read(), type='xml')
target = x.xpath('//Part/Sect/P[contains(@id=, "LinkTarget")]')
tables = target.xpath('Table').extract()
print len(tables)
