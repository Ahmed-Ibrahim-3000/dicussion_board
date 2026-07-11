from django.db import models
from django.contrib.auth.models import User

#python manage.py makemigrations
#python manage.py migrate
# Create your models here.
class Board(models.Model):
  name = models.CharField(
    max_length=50,
    unique=True
    )
  description = models.CharField(
    max_length=150
    )
  def __str__(self):
    return self.name

class Topic(models.Model):
  subject = models.CharField(
    max_length=255
    )
  board = models.ForeignKey(
    Board,
    related_name = 'board_topics',
    on_delete=models.CASCADE
    )
  created_by = models.ForeignKey(
    User,
    related_name='user_topics',
    on_delete=models.CASCADE
    )
  created_dt = models.DateTimeField(
    auto_now_add=True
    )
  def __str__(self):
    return self.subject

class Post(models.Model):
  message = models.TextField(
    max_length=4000
    )
  topic = models.ForeignKey(
    Topic,
    related_name='topic_posts',
    on_delete=models.CASCADE
    )
  created_by = models.ForeignKey(
    User,
    related_name='user_posts',
    on_delete=models.CASCADE
    )
  created_dt = models.DateTimeField(
    auto_now_add=True
    )
  def __str__(self):
    return self.message[0:11]