# Generated by Django 3.1 on 2020-08-24 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200823_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdetail',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ انتهاء العمل'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='if_salary',
            field=models.CharField(blank=True, choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, null=True, verbose_name='هل كنت تعمل بأجر ؟'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='job_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مكان العمل'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المسمى الوظيفي'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='org_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الجهة المشغلة'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='registration_media_act',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration_media_act', to='account.registermediaact'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='salary',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اذكر آخر راتب تقاضيته من هذا العمل'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ بدء العمل'),
        ),
        migrations.AlterField(
            model_name='workdetail',
            name='until_now',
            field=models.CharField(blank=True, choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, null=True, verbose_name='هل تعمل حتى اﻵن ؟'),
        ),
    ]
