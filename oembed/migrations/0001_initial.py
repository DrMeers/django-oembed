# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='name', blank=True)),
                ('regex', models.CharField(max_length=2000, verbose_name='regex')),
                ('endpoint', models.CharField(max_length=2000, verbose_name='endpoint')),
                ('format', models.IntegerField(verbose_name='format', choices=[(1, b'JSON'), (2, b'XML')])),
            ],
        ),
        migrations.CreateModel(
            name='StoredOEmbed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
