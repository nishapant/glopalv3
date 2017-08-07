
from django.contrib.auth.models import Permission, User
from django.db import models


class Activity(models.Model):
    user = models.ForeignKey(User, default=1)
    taskName = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.taskName + ' ' + self.category
#    points = models.CharField(max_length=10)
