

from django.db import models

# Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # add other fields if needed, e.g., course, difficulty

# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

# Submission model
class Submission(models.Model):
    choices = models.ManyToManyField(Choice)
    submitted_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
