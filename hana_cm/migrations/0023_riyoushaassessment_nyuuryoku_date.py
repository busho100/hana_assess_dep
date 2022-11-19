# Generated by Django 4.0.4 on 2022-11-15 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hana_cm', '0022_riyoushaassessment_delete_adl_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='riyoushaassessment',
            name='nyuuryoku_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assess_date', to='hana_cm.riyoushaattributes', verbose_name='入力基準日'),
        ),
    ]
