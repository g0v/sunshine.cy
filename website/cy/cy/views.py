# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from reports.models import Reports
from search.views import hot_keywords, keyword_been_searched, keyword_normalize

def home(request):
    search = keyword_normalize(request.GET)
    if search:
        results = Reports.objects.filter(name=search)
        if results:
            keyword_been_searched(search)
            return redirect(reverse('people:personal_property', kwargs={"name": search, "index": "overview"}))
        results = Reports.objects.filter(department=search)
        if results:
            keyword_been_searched(search)
            return redirect('people/departments/#%s' % search)
        return render(request, 'home.html', {'hot_keywords': hot_keywords(), 'no_results': True})
    return render(request, 'home.html', {'hot_keywords': hot_keywords()})

def about(request):
    return render(request,'about.html', {})

def reference(request):
    return render(request,'reference.html', {})
