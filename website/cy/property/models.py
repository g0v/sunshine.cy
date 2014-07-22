# -*- coding: utf-8 -*-
from django.db import models


class Investment(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    owner = models.TextField()
    company = models.TextField()
    address = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Debt(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    species = models.TextField()
    debtor = models.TextField()
    owner = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Claim(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    species = models.TextField()
    debtor = models.TextField()
    owner = models.TextField()
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Insurance(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    company = models.TextField()
    name = models.TextField()
    owner = models.TextField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Antique(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    name = models.TextField()
    owner = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    total = models.TextField()
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class OtherBonds(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
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

    class Meta:
        unique_together = ('source_file', 'index',)

class Fund(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
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

    class Meta:
        unique_together = ('source_file', 'index',)

class Bonds(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
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

    class Meta:
        unique_together = ('source_file', 'index',)

class Deposit(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    bank = models.TextField()
    deposit_type = models.TextField()
    currency = models.TextField()
    owner = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.total

    class Meta:
        unique_together = ('source_file', 'index',)

class Cash(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    currency = models.TextField()
    owner = models.TextField(blank=True, null=True)
    total = models.FloatField()
    def __unicode__(self):
        return self.total

    class Meta:
        unique_together = ('source_file', 'index',)

class Stock(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    name = models.TextField()
    symbol = models.IntegerField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    trust = models.TextField(blank=True, null=True)
    trust_at = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    face_value = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    currency = models.TextField()
    total = models.FloatField()
    total_value = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Land(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
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

    class Meta:
        unique_together = ('source_file', 'index',)

class Building(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
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

    class Meta:
        unique_together = ('source_file', 'index',)

class Boat(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    name = models.TextField()
    tonnage = models.FloatField()
    homeport = models.TextField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Car(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    name = models.TextField()
    capacity = models.FloatField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)

class Aircraft(models.Model):
    source_file = models.TextField()
    index = models.IntegerField()
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    date = models.DateTimeField()
    category = models.TextField()
    name = models.TextField()
    maker = models.TextField()
    number = models.TextField()
    owner = models.TextField(blank=True, null=True)
    register_date = models.TextField(blank=True, null=True)
    register_reason = models.TextField(blank=True, null=True)
    acquire_value = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('source_file', 'index',)
