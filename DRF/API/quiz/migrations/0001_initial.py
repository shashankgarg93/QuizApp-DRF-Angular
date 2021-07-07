# Generated by Django 3.2.5 on 2021-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=20)),
                ('option2', models.CharField(max_length=20)),
                ('option3', models.CharField(max_length=20)),
                ('option4', models.CharField(max_length=20)),
                ('cans', models.CharField(choices=[(models.CharField(max_length=20), 'Choice 1'), (models.CharField(max_length=20), 'Choice 2'), (models.CharField(max_length=20), 'Choice 3'), (models.CharField(max_length=20), 'Choice 4')], max_length=20)),
            ],
        ),
    ]