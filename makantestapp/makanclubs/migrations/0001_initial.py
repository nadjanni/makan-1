# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Eater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('member_club', models.ForeignKey(to='makanclubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.CharField(max_length=500)),
                ('appreciates', models.IntegerField(default=0)),
                ('experience_date', models.DateTimeField(verbose_name=b'date of experience')),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('reviewer', models.ForeignKey(to='makanclubs.Eater')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='venue',
            field=models.ForeignKey(to='makanclubs.Location'),
        ),
    ]
