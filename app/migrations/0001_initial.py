# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('app_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('app', ['Event'])

        # Adding model 'Demo'
        db.create_table('app_demo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('app', ['Demo'])

        # Adding model 'Comment'
        db.create_table('app_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('app', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('app_event')

        # Deleting model 'Demo'
        db.delete_table('app_demo')

        # Deleting model 'Comment'
        db.delete_table('app_comment')


    models = {
        'app.comment': {
            'Meta': {'object_name': 'Comment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.demo': {
            'Meta': {'object_name': 'Demo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']