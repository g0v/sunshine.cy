# -*- coding: utf-8 -*-
from django.db import models


class Land(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    market_value = models.FloatField(blank=True, null=True)
    area = models.FloatField()
    share_portion = models.TextField()
    portion = models.FloatField()
    owner = models.TextField(blank=True, null=True)
    trust = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Building(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    market_value = models.FloatField(blank=True, null=True)
    area = models.FloatField()
    share_portion = models.TextField()
    portion = models.FloatField()
    owner = models.TextField(blank=True, null=True)
    trust = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Investment(models.Model):
    report = models.ForeignKey('reports.Reports')
    owner = models.TextField()
    company = models.TextField()
    address = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

class Debt(models.Model):
    report = models.ForeignKey('reports.Reports')
    species = models.TextField()
    debtor = models.TextField()
    owner = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

class Claim(models.Model):
    report = models.ForeignKey('reports.Reports')
    species = models.TextField()
    debtor = models.TextField()
    owner = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

class Insurance(models.Model):
    report = models.ForeignKey('reports.Reports')
    company = models.TextField()
    name = models.TextField()
    owner = models.TextField()
    def __unicode__(self):
        return self.name

class Antique(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    owner = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    total = models.TextField()
    def __unicode__(self):
        return self.name

class OtherBonds(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    owner = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    face_value = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    currency = models.TextField()
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Fund(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    owner = models.TextField(blank=True, null=True)
    dealer = models.TextField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    face_value = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    currency = models.TextField()
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Bonds(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    symbol = models.TextField()
    owner = models.TextField(blank=True, null=True)
    dealer = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    face_value = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    currency = models.TextField()
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Deposit(models.Model):
    report = models.ForeignKey('reports.Reports')
    bank = models.TextField()
    deposit_type = models.TextField()
    currency = models.TextField()
    owner = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.total

class Cash(models.Model):
    report = models.ForeignKey('reports.Reports')
    currency = models.TextField()
    owner = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.total

class Stock(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    symbol = models.IntegerField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    trust = models.TextField(blank=True, null=True)
    trust_at = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    face_value = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Boat(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    tonnage = models.FloatField()
    homeport = models.TextField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Car(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    capacity = models.FloatField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Aircraft(models.Model):
    report = models.ForeignKey('reports.Reports')
    name = models.TextField()
    maker = models.TextField()
    number = models.TextField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name
