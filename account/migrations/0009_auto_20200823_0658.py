# Generated by Django 3.1 on 2020-08-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_registermediaact_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportorg',
            name='date_of_response',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ الإحالة '),
        ),
    ]
