# Generated by Django 3.1.1 on 2020-11-09 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_auto_20201109_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]