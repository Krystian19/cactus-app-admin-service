# Generated by Django 2.0.6 on 2018-12-11 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0002_auto_20181206_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='airingTime',
        ),
        migrations.RemoveField(
            model_name='season',
            name='week_day_id',
        ),
        migrations.DeleteModel(
            name='WeekDay',
        ),
    ]