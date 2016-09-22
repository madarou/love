# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findlove', '0002_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='college',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='constellation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='education',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='header',
            field=models.ImageField(null=True, upload_to=b'/img/avatar/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='height',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='hobby',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='hometown',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='pubtime',
            field=models.DateTimeField(null=True),
        ),
    ]
