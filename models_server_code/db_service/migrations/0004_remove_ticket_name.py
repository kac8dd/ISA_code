# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_service', '0003_auto_20151002_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
    ]
