# Generated by Django 3.0 on 2019-12-25 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0018_auto_20191225_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 583872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 583872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 584900, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 585894, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 587889, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 33, 37, 587889, tzinfo=utc)),
        ),
    ]
