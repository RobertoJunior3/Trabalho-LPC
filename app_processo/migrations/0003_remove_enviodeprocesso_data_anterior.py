# Generated by Django 2.2 on 2019-10-04 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_processo', '0002_auto_20191004_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enviodeprocesso',
            name='data_anterior',
        ),
    ]
