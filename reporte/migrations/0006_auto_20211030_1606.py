# Generated by Django 3.1.3 on 2021-10-30 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0005_auto_20210801_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humedal',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
