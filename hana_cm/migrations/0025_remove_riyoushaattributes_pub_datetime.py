# Generated by Django 4.0.4 on 2022-11-22 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hana_cm', '0024_alter_riyoushaassessment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riyoushaattributes',
            name='pub_datetime',
        ),
    ]
