# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostUserRating'
        db.create_table(u'spotit_postuserrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['spotit.Post'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post_ratings', to=orm['core.User'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'spotit', ['PostUserRating'])

        # Adding model 'PostCommentUserRating'
        db.create_table(u'spotit_postcommentuserrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_comment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['spotit.PostComment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post_comment_ratings', to=orm['core.User'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'spotit', ['PostCommentUserRating'])

        # Adding model 'PostPhoto'
        db.create_table(u'spotit_postphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['spotit.Post'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 14, 0, 0))),
        ))
        db.send_create_signal(u'spotit', ['PostPhoto'])


    def backwards(self, orm):
        # Deleting model 'PostUserRating'
        db.delete_table(u'spotit_postuserrating')

        # Deleting model 'PostCommentUserRating'
        db.delete_table(u'spotit_postcommentuserrating')

        # Deleting model 'PostPhoto'
        db.delete_table(u'spotit_postphoto')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.user': {
            'Meta': {'unique_together': "(('email',), ('phone_number',))", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'spotit.post': {
            'Meta': {'ordering': "['-date_add']", 'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['core.User']"}),
            'author_ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count_comments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count_vote': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'spotit.postcomment': {
            'Meta': {'ordering': "['date_add']", 'object_name': 'PostComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_comments'", 'to': u"orm['core.User']"}),
            'author_ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count_vote': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 14, 0, 0)'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['spotit.Post']"}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'spotit.postcommentuserrating': {
            'Meta': {'object_name': 'PostCommentUserRating'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': u"orm['spotit.PostComment']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_comment_ratings'", 'to': u"orm['core.User']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {})
        },
        u'spotit.postphoto': {
            'Meta': {'ordering': "['-date_add']", 'object_name': 'PostPhoto'},
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['spotit.Post']"})
        },
        u'spotit.postuserrating': {
            'Meta': {'object_name': 'PostUserRating'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': u"orm['spotit.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_ratings'", 'to': u"orm['core.User']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['spotit']