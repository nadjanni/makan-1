# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('makanclubs', '0003_auto_20150613_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='club',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='eater',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='location',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
    ]
