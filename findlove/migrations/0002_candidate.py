# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findlove', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'/img/avatar/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
