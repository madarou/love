# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findlove', '0004_candidate_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='weight',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
