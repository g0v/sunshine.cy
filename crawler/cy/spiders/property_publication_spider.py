# -*- coding: utf-8 -*-
import os
import re
import subprocess
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from cy.items import PropertyItem


class Spider(scrapy.Spider):
    name = "property"
    allowed_domains = ["sunshine.cy.gov.tw"]
    start_urls = ['http://sunshine.cy.gov.tw/GipOpenWeb/wSite/lp?ctNode=442&mp=2&nowPage=1&pagesize=300']

    def parse(self, response):
        sel = Selector(response)
        items = []
        trs = sel.xpath('//table[@class="lptb3"]/tr')
        for tr in trs:
            tds = tr.xpath('td')
            if tds:
                item = PropertyItem()
                item['name'] = tds[1].xpath('text()').re(u'\s*(\S+)\s*')[0]
                item['date'] = re.sub('/', '-', tds[2].xpath('text()').extract()[0])
                item['download_url'] = ['http://sunshine.cy.gov.tw/GipOpenWeb/wSite/%s' % link for link in tds[3].xpath('div/a/@href').extract()]
                for link in item['download_url']:
                    # -N for ignoring existed files
                    cmd = 'wget -Nc -O ../data/pdf/journal/%s.pdf %s' % (item['name'], link)
                    retcode = subprocess.call(cmd, shell=True)
                items.append(item)
        return items
