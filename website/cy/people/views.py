# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
from django.db.models import Count, Sum, F, Q
from reports.models import Reports
from property.models import Stock, Land, Building, Car, Cash, Deposit, Bonds, Fund, OtherBonds, Antique, Insurance, Claim, Debt, Investment


def departments(request):
    objs = Reports.objects.values('department', 'name', 'title').distinct().order_by('department', 'name', 'title')
    return render(request,'people/departments.html', {'objs': objs})

def personal_property(request, name, index):
    attribute = {
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
    summaries = []
    reports = Reports.objects.filter(name=name).order_by('-report_at')
    if not reports:
        return render(request,'people/not_exist.html', {'name': name})
    reports_can_calc = reports.filter(report_at__isnull=False)
    if reports_can_calc:
        person = reports_can_calc[0]
    else:
        person = reports[0]
    date_union = reports_can_calc.values_list('report_at', flat=True).distinct()
    if index == 'overview':
        for key, value in attribute.items():
            if value.get('sum'):
                objs = value.get('model').objects.filter(report_id__in=reports_can_calc.values_list('id', flat=True))\
                                                 .order_by('-report__report_at')\
                                                 .values('report__report_at')\
                                                 .annotate(total=Sum(value.get('sum')), count=Count('id'))
            else:
                objs = value.get('model').objects.filter(report_id__in=reports_can_calc.values_list('id', flat=True))\
                                                 .order_by('-report__report_at')\
                                                 .values('report__report_at')\
                                                 .annotate(count=Count('id'))
            for obj in objs:
                obj['index'] = key
            if objs:
                summaries.append(list(objs))
        for category in summaries:
            date_exist = [item['report__report_at'] for item in category]
            key = category[0]['index']
            for date in date_union:
                if date not in date_exist:
                    category.append({'report__report_at': date, 'totol': None, 'index': key})
            category.sort(key = lambda x: x['report__report_at'], reverse=True)
        return render(request,'people/personal_property_overview.html', {'reports': reports, 'person': person,  'summaries': summaries, 'date_union': date_union, 'index': index})
    else:
        objs = attribute.get(index).get('model').objects.filter(report_id__in=reports_can_calc.values_list('id', flat=True)).order_by('-report__report_at')
        if attribute.get(index).get('sum'):
            summaries = objs.values('report__report_at').annotate(total=Sum(attribute.get(index).get('sum')), count=Count('id'))
        else:
            summaries = objs.values('report__report_at').annotate(count=Count('id'))
        return render(request,'people/personal_property.html', {'reports': reports, 'person': person, 'objs': objs, 'summaries': summaries, 'index': index, 'cht': attribute.get(index).get('cht')})

