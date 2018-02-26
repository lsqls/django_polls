# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")
    def __unicode__(self):
        return self.question_text
class choice(models.Model):
    question=models.ForeignKey(question)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
