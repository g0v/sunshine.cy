# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stock.fullname'
        db.add_column(u'property_stock', 'fullname',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stock.fullname'
        db.delete_column(u'property_stock', 'fullname')


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
            'fullname': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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