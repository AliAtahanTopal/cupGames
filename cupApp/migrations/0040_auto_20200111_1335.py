# Generated by Django 3.0.2 on 2020-01-11 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0039_auto_20200111_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresubmission',
            name='proof',
            field=models.TextField(default='No Link'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 180292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 180292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 181291, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 182292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scoresubmission',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 185302, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 184302, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 10, 35, 32, 184302, tzinfo=utc)),
        ),
    ]
