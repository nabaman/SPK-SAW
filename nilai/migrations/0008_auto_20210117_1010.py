# Generated by Django 3.1.5 on 2021-01-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilai', '0007_auto_20210117_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_krips',
            name='kriteria',
        ),
        migrations.AddField(
            model_name='data_kriteria',
            name='krips',
            field=models.ManyToManyField(to='nilai.Data_Krips'),
        ),
    ]
