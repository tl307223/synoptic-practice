# Generated by Django 3.1.7 on 2021-05-04 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuizManager', '0011_auto_20210504_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='assigned_users',
            field=models.ManyToManyField(blank=True, related_name='assigned_quizzes', to=settings.AUTH_USER_MODEL),
        ),
    ]