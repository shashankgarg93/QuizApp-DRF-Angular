# Generated by Django 3.2.5 on 2021-07-07 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_user', '0002_auto_20210707_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='user',
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
