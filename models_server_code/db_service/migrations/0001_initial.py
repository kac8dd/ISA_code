# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=5000)),
                ('start_time', models.DateTimeField(default=datetime.datetime.today)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.today)),
                ('location', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
                ('event', models.ForeignKey(to='db_service.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(unique=True, max_length=24)),
                ('date_joined', models.DateTimeField()),
                ('firstname', models.CharField(max_length=16)),
                ('lastname', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=96)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchase',
            name='buyer',
            field=models.OneToOneField(to='db_service.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='ticket',
            field=models.OneToOneField(to='db_service.Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(to='db_service.User'),
            preserve_default=True,
        ),
    ]
