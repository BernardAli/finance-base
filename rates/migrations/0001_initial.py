# Generated by Django 3.2.5 on 2021-07-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inflation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
