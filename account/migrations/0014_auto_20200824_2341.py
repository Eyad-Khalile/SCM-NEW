# Generated by Django 3.1 on 2020-08-24 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200824_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='violation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.registermediaact'),
        ),
    ]
