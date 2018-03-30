from django.db import models


class School(models.Model):
    schoolName = models.CharField(max_length=140)
    location = models.TextField()

    def __str__(self):
        return self.schoolName
