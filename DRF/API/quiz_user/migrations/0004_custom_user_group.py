# Generated by Django 3.2.5 on 2021-07-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_user', '0003_auto_20210707_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='group',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
