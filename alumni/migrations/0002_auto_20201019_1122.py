# Generated by Django 3.1.1 on 2020-10-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='avatar',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
