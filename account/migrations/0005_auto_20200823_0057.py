# Generated by Django 3.1 on 2020-08-23 00:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200822_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support_descrption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppo', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الجهة الداعمة')),
                ('suppo_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='وصف حول الجهة')),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterMediaAct',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='تاريخ الميلاد'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_place',
            field=models.CharField(max_length=255, null=True, verbose_name='مكان الولادة'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(max_length=255, null=True, verbose_name='من أي دولة ؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_country',
            field=django_countries.fields.CountryField(max_length=255, null=True, verbose_name='في أي دولة ؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_region',
            field=models.CharField(blank=True, choices=[('aleppo', 'حلب'), ('damascus', 'دمشق'), ('suburb of damascus', 'ريف دمشق'), ('daraa', 'درعا'), ('deir ez-Zor', 'دير الزور'), ('hama', 'حماه'), ('al-Hasakah', 'الحسكة'), ('homs', 'حمص'), ('idlib', 'إدلب'), ('latakia', 'اللاذقية'), ('quneitra', 'القنيطرة'), ('raqqa', 'الرقة'), ('as-Suwayda', 'السويداء'), ('tartus', 'طرطوس')], max_length=100, null=True, verbose_name='في أي محافظة ؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='صفحة الفيسبوك'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='الاسم المستعار'),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, choices=[('aleppo', 'حلب'), ('damascus', 'دمشق'), ('suburb of damascus', 'ريف دمشق'), ('daraa', 'درعا'), ('deir ez-Zor', 'دير الزور'), ('hama', 'حماه'), ('al-Hasakah', 'الحسكة'), ('homs', 'حمص'), ('idlib', 'إدلب'), ('latakia', 'اللاذقية'), ('quneitra', 'القنيطرة'), ('raqqa', 'الرقة'), ('as-Suwayda', 'السويداء'), ('tartus', 'طرطوس')], max_length=100, null=True, verbose_name='من أي محافظة ؟'),
        ),
    ]
