# Generated by Django 3.1.5 on 2021-01-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilai', '0012_auto_20210117_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_karyawan',
            name='skor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]