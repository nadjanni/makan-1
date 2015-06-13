# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('makanclubs', '0002_auto_20150613_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eater',
            name='member_club',
        ),
        migrations.AlterField(
            model_name='club',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 54, 8, 171220, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='eater',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 54, 8, 171872, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 54, 8, 172666, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='location',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 54, 8, 172230, tzinfo=utc), verbose_name=b'date created'),
        ),
    ]
