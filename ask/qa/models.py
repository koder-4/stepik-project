from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_queryset().order_by('-added_at')

    def popular(self):
        return super(QuestionManager, self).get_queryset().annotate(models.Count('likes')).order_by('likes__count')
		

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank = True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='question_author', default=None)
	likes = models.ManyToManyField(User)
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None)
	