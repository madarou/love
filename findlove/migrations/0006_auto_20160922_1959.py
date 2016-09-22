# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findlove', '0005_candidate_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='photos',
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo1',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo10',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo2',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo3',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo4',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo5',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo6',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo7',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo8',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo9',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/photos/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/avatar/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='header',
            field=models.ImageField(null=True, upload_to=b'findlove/static/public/img/header/'),
        ),
    ]
