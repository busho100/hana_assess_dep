# Generated by Django 4.0.4 on 2022-10-15 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hana_cm', '0018_remove_riyoushaattributes_examination_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='riyoushaattributes',
            name='examination_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hana_cm.ExaminationStatus+', to='hana_cm.examinationstatus', verbose_name='診察状況'),
        ),
    ]
