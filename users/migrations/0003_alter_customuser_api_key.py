# Generated by Django 3.2.5 on 2022-08-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220813_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='api_key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
