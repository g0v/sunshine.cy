# -*- coding: utf-8 -*-
from django.db import models


class Reports(models.Model):
    journal = models.ForeignKey('journals.Journals', to_field="name")
    category = models.TextField()
    name = models.TextField()
    department = models.TextField()
    title = models.TextField()
    report_at = models.DateField()
    report_type = models.TextField()
    spouse = models.TextField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('journal', 'category', 'name', 'report_at', 'report_type',)
