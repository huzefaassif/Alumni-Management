# Generated by Django 3.1.1 on 2020-10-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20201022_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='noofviews',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]