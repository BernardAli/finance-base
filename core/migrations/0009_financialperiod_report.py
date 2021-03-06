# Generated by Django 3.2.5 on 2021-07-17 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_companyprofile_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('Q1', '1st Quarter'), ('H1', '1st Half'), ('9M', '9 Months'), ('FY', 'Full Year')], max_length=50)),
                ('slug', models.SlugField(default='fy', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('file', models.FileField(upload_to='reports')),
                ('audited', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.companyprofile')),
                ('period', models.ManyToManyField(to='core.FinancialPeriod')),
            ],
        ),
    ]
