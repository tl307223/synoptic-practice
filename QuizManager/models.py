from django.db import models

from django.contrib.auth import get_user_model


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=30)
    assigned_users = models.ManyToManyField(get_user_model(), blank=True, related_name="assigned_quizzes")
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, 
        on_delete=models.CASCADE,
        related_name='questions'
        )
    question_text = models.CharField(max_length=300)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    choice_text = models.CharField(max_length=300)
    correct = models.BooleanField()
    def __str__(self):
        return self.choice_text

class Result(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)
    