# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findlove', '0003_auto_20160922_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
