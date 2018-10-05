from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model)
	title = models.CharField(maxlength=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=False, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User)
	
class Answer(models.Model)
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	