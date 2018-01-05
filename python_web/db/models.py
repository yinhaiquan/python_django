# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()
    desc = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.name+","+str(self.age)+","+self.email