# Generated by Django 3.0.2 on 2020-01-09 04:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0034_auto_20200107_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 261755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 261755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 265767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 265767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 270271, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 4, 38, 25, 270271, tzinfo=utc)),
        ),
    ]
