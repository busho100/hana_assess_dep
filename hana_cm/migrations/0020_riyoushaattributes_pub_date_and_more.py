# Generated by Django 4.0.4 on 2022-10-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hana_cm', '0019_riyoushaattributes_examination_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='riyoushaattributes',
            name='pub_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='riyoushaattributes',
            name='pub_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]