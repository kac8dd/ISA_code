# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.OneToOneField(default=1, to='db_service.UserProfile'),
            preserve_default=False,
        ),
    ]
