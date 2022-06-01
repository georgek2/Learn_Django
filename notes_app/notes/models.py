from django.db import models

# Create your models here.


# Table links topic to the obj, aim and target


class Topic(models.Model):

    title = models.CharField(max_length=200)

    week = models.CharField(max_length=200)

    objective = models.TextField()

    aim = models.TextField()

    target = models.TextField()


    def __str__(self):

        return self.title


class Output(models.Model):
    
    foreign = models.ForeignKey('Topic', on_delete=models.CASCADE)
    topic = models.CharField(max_length=20)
    takeaway = models.TextField()
    applications = models.TextField()


    def __str__(self):

        return self.topic


class User(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # confirm = models.CharField(max_length=20)

    def __str__(self):

        return self.username

