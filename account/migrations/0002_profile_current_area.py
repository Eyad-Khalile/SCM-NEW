# Generated by Django 2.2.12 on 2020-08-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_area',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='من اي منطقة ؟'),
        ),
    ]
