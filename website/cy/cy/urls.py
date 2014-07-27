from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^ranking/', include('ranking.urls', namespace="ranking")),
    url(r'^about/$', 'cy.views.about', name='about'),
    url(r'^reference/$', 'cy.views.reference', name='reference'),
    url(r'', 'cy.views.home', name='home'),
)
