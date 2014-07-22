# -*- coding: utf-8 -*-
from django.db import models


class Journals(models.Model):
    name = models.TextField(unique=True)
    date = models.DateField()
    download_url = models.TextField()
    def __unicode__(self):
        return self.name
