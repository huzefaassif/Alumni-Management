# Generated by Django 3.1.1 on 2020-10-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0008_auto_20201029_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='About_you',
            field=models.CharField(default='', max_length=150),
        ),
    ]