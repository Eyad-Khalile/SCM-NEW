# Generated by Django 3.0.4 on 2020-08-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200823_0700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docs',
            options={'verbose_name': ' ارفاق  ملفات'},
        ),
        migrations.AlterField(
            model_name='registermediaact',
            name='know_support_programme',
            field=models.TextField(max_length=1500, verbose_name='كيف علمت ببرنامجنا للدعم ؟'),
        ),
    ]
