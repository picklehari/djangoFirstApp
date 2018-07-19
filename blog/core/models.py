from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    def publish(self):
        self.save()
    def __str__(self):
        return self.title
