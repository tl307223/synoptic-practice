# Generated by Django 3.1.7 on 2021-04-30 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizManager', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assigned_quizzes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_quizzes', to='QuizManager.quiz'),
        ),
    ]
