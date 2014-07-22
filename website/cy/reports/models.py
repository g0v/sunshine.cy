# -*- coding: utf-8 -*-
from django.db import models


class Reports(models.Model):
    journal = models.ForeignKey('journals.Journals', to_field="uid")
    name = models.TextField()
    department = models.IntegerField()
    report_at = models.ForeignKey('legislator.Legislator', to_field="uid")
    report_type = models.DateTimeField()
    spouse = models.TextField()
    def __unicode__(self):
        return self.name
