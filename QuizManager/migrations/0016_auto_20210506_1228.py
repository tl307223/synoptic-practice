# Generated by Django 3.1.7 on 2021-05-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizManager', '0015_auto_20210505_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(),
        ),
    ]
