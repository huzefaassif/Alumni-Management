# Generated by Django 3.1.1 on 2020-11-09 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0010_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='date',
        ),
        migrations.AddField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
