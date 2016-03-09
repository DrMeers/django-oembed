# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='name')),
                ('regex', models.CharField(max_length=2000, verbose_name='regex')),
                ('endpoint', models.CharField(max_length=2000, verbose_name='endpoint')),
                ('format', models.IntegerField(choices=[(1, b'JSON'), (2, b'XML')], verbose_name='format')),
            ],
        ),
        migrations.CreateModel(
            name='StoredOEmbed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.TextField(verbose_name='match')),
                ('max_width', models.IntegerField(verbose_name='max width')),
                ('max_height', models.IntegerField(verbose_name='max height')),
                ('html', models.TextField(verbose_name='html')),
                ('json', models.TextField(verbose_name='json')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
            ],
            options={
                'ordering': ('-max_width',),
            },
        ),
    ]
