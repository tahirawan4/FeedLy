# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-17 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('feed_id', models.CharField(max_length=200)),
                ('origin_url', models.CharField(max_length=500)),
                ('published_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('summary', models.TextField()),
                ('engagement', models.IntegerField(default=0)),
                ('engagement_rate', models.FloatField(default=0.0)),
                ('is_hidden', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('is_hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.CharField(max_length=500)),
                ('stream_title', models.CharField(max_length=200)),
                ('is_hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='parser.Keyword'),
        ),
        migrations.AddField(
            model_name='feed',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.Stream'),
        ),
    ]
