# Generated by Django 3.0.4 on 2020-09-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200903_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportorgchild',
            name='result_of_org',
            field=models.CharField(blank=True, choices=[('0', 'مقبول'), ('1', 'مرفوض'), ('2', 'قيد الدراسة ')], default=False, max_length=255, null=True, verbose_name='النتيجة'),
        ),
        migrations.DeleteModel(
            name='SupportOrg',
        ),
    ]