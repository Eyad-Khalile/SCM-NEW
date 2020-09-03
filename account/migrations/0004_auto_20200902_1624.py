# Generated by Django 3.0.4 on 2020-09-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200902_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportorgchild',
            name='date_of_response',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ اﻹحالة'),
        ),
        migrations.AddField(
            model_name='supportorgchild',
            name='date_of_result',
            field=models.DateField(blank=True, null=True, verbose_name=' تاريخ الاستجابة '),
        ),
        migrations.AddField(
            model_name='supportorgchild',
            name='result_of_org',
            field=models.CharField(blank=True, choices=[('0', 'مقبول'), ('1', 'مرفوض')], default=False, max_length=255, null=True, verbose_name='النتيجة'),
        ),
    ]