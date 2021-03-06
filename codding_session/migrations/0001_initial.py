# Generated by Django 2.2.14 on 2021-04-03 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoddingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True)),
                ('language', models.CharField(max_length=1024)),
                ('link', models.CharField(max_length=2048)),
                ('starting_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
