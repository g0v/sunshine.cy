# -*- coding: utf-8 -*-
import re
from django.db.models import F
from search.models import Keyword


def keyword_list(category):
    # 1: proposal, 2: vote, 3: bill
    return list(Keyword.objects.filter(category=category,valid=True).order_by('-hits').values_list('content', flat=True))

def keyword_been_searched(keyword, category):
    keyword_obj = Keyword.objects.filter(category=category, content=keyword)
    if keyword_obj:
        keyword_obj.update(hits=F('hits')+1)
    else:
        k = Keyword(content=keyword, category=category, valid=True, hits=1)
        k.save()

def keyword_normalize(request, keyword_url):
    if 'keyword' in request.GET:
        return re.sub(u'[，。／＼、；］［＝－＜＞？：＂｛｝｜＋＿（）！＠＃％＄︿＆＊～~`!@#$%^&*_+\-=,./<>?;:\'"\[\]{}\|()]',' ',request.GET['keyword']).strip()
    elif keyword_url:
        return keyword_url.strip()
