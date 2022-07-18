from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):


    def __str__(self):
        return self.username

class Puzzle(models.Model):
    title       = models.CharField(max_length=255,blank=True)
    date        = models.DateField()
    byline      = models.CharField(max_length=255)    
    publisher   = models.CharField(max_length=12)   

    def __str__(self):
        return self.title


class Entry(models.Model):
    entry_text  = models.CharField(max_length=50)

class Clue(models.Model):
    entry       = models.ForeignKey('Entry', related_name='clues', on_delete=models.CASCADE)
    puzzle      = models.ForeignKey('Puzzle',related_name='puzzle_clues', on_delete=models.CASCADE)
    clue_text   = models.CharField(max_length=512)
    theme       = models.BooleanField(default=False,null=True, blank=True)

    
    class Meta:
     

        def __str__(self):
            return self.name
