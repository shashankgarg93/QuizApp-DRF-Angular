# Generated by Django 3.2.5 on 2021-07-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_user', '0004_custom_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]