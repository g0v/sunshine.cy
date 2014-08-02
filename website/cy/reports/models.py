# -*- coding: utf-8 -*-
from django.db import models


class Reports(models.Model):
    journal = models.ForeignKey('journals.Journals', to_field="name", blank=True, null=True)
    category = models.TextField()
    name = models.TextField()
    department = models.TextField()
    title = models.TextField()
    report_at = models.DateField(blank=True, null=True)
    report_type = models.TextField(blank=True, null=True)
    spouse = models.TextField(blank=True, null=True)
    download_url = models.TextField(blank=True, null=True)
    at_page = models.TextField(blank=True, null=True)
    file_id = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name
