# Generated by Django 3.2.5 on 2021-07-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_companyprofile_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='summary',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
