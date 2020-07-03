# Generated by Django 3.0.6 on 2020-05-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledge_base',
            name='title',
        ),
        migrations.AddField(
            model_name='knowledge_base',
            name='number_cwe',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]