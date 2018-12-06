# Generated by Django 2.0.6 on 2018-12-06 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'WeekDays',
            },
        ),
        migrations.AddField(
            model_name='season',
            name='airingTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='week_day_id',
            field=models.ForeignKey(blank=True, db_column='week_day_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='Anime.WeekDay'),
        ),
    ]