from django.db import models
from django.utils import timezone
import datetime
# Create your models here. LATER THIS IS THE DATABASE
class Question(models.Model):
    #column name=datatype
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #change value displayed for Question.objects.all()
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #each choice is associated with 1 question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
