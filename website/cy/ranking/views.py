# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.db.models import Count, Sum, F, Q
from reports.models import Reports
from property.models import Stock, Land, Building, Car, Cash, Deposit, Bonds, Fund, OtherBonds, Antique, Insurance, Claim, Debt, Investment


def ranking_by_property(request, index):
    attr = {
        'land': {
            'model': Land,
            'sum': 'total',
            'cht': u'土地'
        },
        'building': {
            'model': Building,
            'sum': 'total',
            'cht': u'建物'
        },
        'stock': {
            'model': Stock,
            'sum': 'total',
            'cht': u'股票'
        },
        'car': {
            'model': Car,
            'sum': 'capacity',
            'cht': u'汽車'
        },
        'cash': {
            'model': Cash,
            'sum': 'total',
            'cht': u'現金'
        },
        'deposit': {
            'model': Deposit,
            'sum': 'total',
            'cht': u'存款'
        },
        'bonds': {
            'model': Bonds,
            'sum': 'total',
            'cht': u'債券'
        },
        'fund': {
            'model': Fund,
            'sum': 'total',
            'cht': u'基金'
        },
        'otherbonds': {
            'model': OtherBonds,
            'sum': 'total',
            'cht': u'其他有價證券'
        },
        'antique': {
            'model': Antique,
            'cht': u'具有相當價值之財產'
        },
        'insurance': {
            'model': Insurance,
            'cht': u'保險'
        },
        'claim': {
            'model': Claim,
            'sum': 'total',
            'cht': u'債權'
        },
        'debt': {
            'model': Debt,
            'sum': 'total',
            'cht': u'債務'
        },
        'investment': {
            'model': Investment,
            'sum': 'total',
            'cht': u'事業投資'
        }
    }
    if attr.get(index):
        objs = attr[index]['model'].objects.extra(select={'year': "EXTRACT(year FROM report__report_at)"})\
                                           .values('report__name', 'year')\
                                           .annotate(totalNum=Sum(attr[index]['sum']))\
                                           .order_by('-totalNum')
        print objs
    return render(request, 'about.html', {})
