# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Land'
        db.create_table(u'property_land', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('share_portion', self.gf('django.db.models.fields.TextField')()),
            ('portion', self.gf('django.db.models.fields.FloatField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('trust', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acquire_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Land'])

        # Adding model 'Building'
        db.create_table(u'property_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.TextField')()),
            ('share_portion', self.gf('django.db.models.fields.TextField')()),
            ('portion', self.gf('django.db.models.fields.FloatField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('trust', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acquire_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Building'])

        # Adding model 'Boat'
        db.create_table(u'property_boat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('tonnage', self.gf('django.db.models.fields.FloatField')()),
            ('homeport', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acquire_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Boat'])

        # Adding model 'Car'
        db.create_table(u'property_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('capacity', self.gf('django.db.models.fields.FloatField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acquire_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Car'])

        # Adding model 'Aircraft'
        db.create_table(u'property_aircraft', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('maker', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acquire_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Aircraft'])

        # Adding model 'Cash'
        db.create_table(u'property_cash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('currency', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('currency_total', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'property', ['Cash'])

        # Adding model 'Deposit'
        db.create_table(u'property_deposit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('bank', self.gf('django.db.models.fields.TextField')()),
            ('deposit_type', self.gf('django.db.models.fields.TextField')()),
            ('currency', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('currency_total', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'property', ['Deposit'])

        # Adding model 'Stock'
        db.create_table(u'property_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('symbol', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('trust', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('trust_at', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('face_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Stock'])

        # Adding model 'Bonds'
        db.create_table(u'property_bonds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('symbol', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('dealer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('face_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.TextField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Bonds'])

        # Adding model 'Fund'
        db.create_table(u'property_fund', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('dealer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('face_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.TextField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['Fund'])

        # Adding model 'OtherBonds'
        db.create_table(u'property_otherbonds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('face_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('market_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.TextField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('total_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'property', ['OtherBonds'])

        # Adding model 'Antique'
        db.create_table(u'property_antique', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'property', ['Antique'])

        # Adding model 'Insurance'
        db.create_table(u'property_insurance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('company', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'property', ['Insurance'])

        # Adding model 'Claim'
        db.create_table(u'property_claim', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('species', self.gf('django.db.models.fields.TextField')()),
            ('debtor', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')()),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'property', ['Claim'])

        # Adding model 'Debt'
        db.create_table(u'property_debt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('species', self.gf('django.db.models.fields.TextField')()),
            ('debtor', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.TextField')()),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'property', ['Debt'])

        # Adding model 'Investment'
        db.create_table(u'property_investment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Reports'])),
            ('owner', self.gf('django.db.models.fields.TextField')()),
            ('company', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('register_date', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('register_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'property', ['Investment'])


    def backwards(self, orm):
        # Deleting model 'Land'
        db.delete_table(u'property_land')

        # Deleting model 'Building'
        db.delete_table(u'property_building')

        # Deleting model 'Boat'
        db.delete_table(u'property_boat')

        # Deleting model 'Car'
        db.delete_table(u'property_car')

        # Deleting model 'Aircraft'
        db.delete_table(u'property_aircraft')

        # Deleting model 'Cash'
        db.delete_table(u'property_cash')

        # Deleting model 'Deposit'
        db.delete_table(u'property_deposit')

        # Deleting model 'Stock'
        db.delete_table(u'property_stock')

        # Deleting model 'Bonds'
        db.delete_table(u'property_bonds')

        # Deleting model 'Fund'
        db.delete_table(u'property_fund')

        # Deleting model 'OtherBonds'
        db.delete_table(u'property_otherbonds')

        # Deleting model 'Antique'
        db.delete_table(u'property_antique')

        # Deleting model 'Insurance'
        db.delete_table(u'property_insurance')

        # Deleting model 'Claim'
        db.delete_table(u'property_claim')

        # Deleting model 'Debt'
        db.delete_table(u'property_debt')

        # Deleting model 'Investment'
        db.delete_table(u'property_investment')


    models = {
        u'journals.journals': {
            'Meta': {'object_name': 'Journals'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'download_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'property.aircraft': {
            'Meta': {'object_name': 'Aircraft'},
            'acquire_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maker': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"})
        },
        u'property.antique': {
            'Meta': {'object_name': 'Antique'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.TextField', [], {})
        },
        u'property.boat': {
            'Meta': {'object_name': 'Boat'},
            'acquire_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'homeport': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'tonnage': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.bonds': {
            'Meta': {'object_name': 'Bonds'},
            'currency': ('django.db.models.fields.TextField', [], {}),
            'dealer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'face_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'symbol': ('django.db.models.fields.TextField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'property.building': {
            'Meta': {'object_name': 'Building'},
            'acquire_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'portion': ('django.db.models.fields.FloatField', [], {}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'share_portion': ('django.db.models.fields.TextField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trust': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'property.car': {
            'Meta': {'object_name': 'Car'},
            'acquire_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"})
        },
        u'property.cash': {
            'Meta': {'object_name': 'Cash'},
            'currency': ('django.db.models.fields.TextField', [], {}),
            'currency_total': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.claim': {
            'Meta': {'object_name': 'Claim'},
            'debtor': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'species': ('django.db.models.fields.TextField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.debt': {
            'Meta': {'object_name': 'Debt'},
            'debtor': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'species': ('django.db.models.fields.TextField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.deposit': {
            'Meta': {'object_name': 'Deposit'},
            'bank': ('django.db.models.fields.TextField', [], {}),
            'currency': ('django.db.models.fields.TextField', [], {}),
            'currency_total': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'deposit_type': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.fund': {
            'Meta': {'object_name': 'Fund'},
            'currency': ('django.db.models.fields.TextField', [], {}),
            'dealer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'face_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'property.insurance': {
            'Meta': {'object_name': 'Insurance'},
            'company': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"})
        },
        u'property.investment': {
            'Meta': {'object_name': 'Investment'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'property.land': {
            'Meta': {'object_name': 'Land'},
            'acquire_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'portion': ('django.db.models.fields.FloatField', [], {}),
            'register_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'share_portion': ('django.db.models.fields.TextField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trust': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'property.otherbonds': {
            'Meta': {'object_name': 'OtherBonds'},
            'currency': ('django.db.models.fields.TextField', [], {}),
            'face_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'property.stock': {
            'Meta': {'object_name': 'Stock'},
            'currency': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'face_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Reports']"}),
            'symbol': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'total_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trust': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'trust_at': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.reports': {
            'Meta': {'object_name': 'Reports'},
            'at_page': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.TextField', [], {}),
            'department': ('django.db.models.fields.TextField', [], {}),
            'download_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['journals.Journals']", 'to_field': "'name'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'report_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'report_type': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'spouse': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['property']