# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_service', '0002_auto_20151020_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(primary_key=True, max_length=100, serialize=False),
            preserve_default=True,
        ),
    ]
