from django.db import models

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()

    def __unicode__(self):
        return self.title