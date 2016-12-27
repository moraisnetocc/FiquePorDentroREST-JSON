from django.db import models


class InfoCategory(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    category = models.ForeignKey(InfoCategory, related_name='infos')

    def __unicode__(self):
        return self.title
