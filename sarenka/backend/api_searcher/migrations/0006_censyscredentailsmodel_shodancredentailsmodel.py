# Generated by Django 3.1.4 on 2021-01-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_searcher', '0005_auto_20210105_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensysCredentailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(default='', max_length=72, unique=True)),
                ('secret', models.CharField(default='', max_length=64, unique=True)),
                ('base_url', models.CharField(default='https://censys.io/', max_length=36, unique=True)),
                ('api_url', models.CharField(default='https://censys.io/api/v1', max_length=48, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShodanCredentailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=200, unique=True)),
                ('api_key', models.CharField(default='', max_length=64, unique=True)),
                ('base_url', models.CharField(default='https://www.shodan.io/', max_length=44, unique=True)),
            ],
        ),
    ]
