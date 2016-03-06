from django.db import models

from django.contrib.auth.models import User


class Question(models.Model):

    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'answers'
        ordering = ['-added_at']
