# Generated by Django 3.1.1 on 2020-10-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0006_auto_20201027_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='About_you',
            field=models.CharField(max_length=200),
        ),
    ]
