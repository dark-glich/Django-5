# Generated by Django 3.1.7 on 2021-03-07 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
