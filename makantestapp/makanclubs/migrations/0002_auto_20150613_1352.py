# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('makanclubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='club',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 52, 48, 217274, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='eater',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 52, 48, 217914, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 52, 48, 218748, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='location',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 52, 48, 218314, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AddField(
            model_name='membership',
            name='club',
            field=models.ForeignKey(to='makanclubs.Club'),
        ),
        migrations.AddField(
            model_name='membership',
            name='eater',
            field=models.ForeignKey(to='makanclubs.Eater'),
        ),
    ]
