# Generated by Django 3.2.5 on 2021-07-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_financialperiod_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
