from django.db import models

# Create your models here.


# Table links topic to the obj, aim and target


class Topic(models.Model):

    title = models.CharField(max_length=200)

    objective = models.TextField()

    aim = models.TextField()

    target = models.TextField()


    def __str__(self):

        return self.title









