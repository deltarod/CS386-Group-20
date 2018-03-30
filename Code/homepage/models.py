from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

