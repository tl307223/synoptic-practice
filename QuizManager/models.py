from django.db import models

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=30)
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