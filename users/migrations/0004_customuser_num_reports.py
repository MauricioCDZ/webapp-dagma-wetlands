# Generated by Django 3.1.3 on 2021-04-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_num_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='num_reports',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
