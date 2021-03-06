# Generated by Django 3.0.2 on 2020-01-11 09:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0038_auto_20200111_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 37553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 37553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 38563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 39563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scoresubmission',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 42554, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 41555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 9, 50, 56, 41555, tzinfo=utc)),
        ),
    ]
