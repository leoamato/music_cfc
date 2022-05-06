from django.db import models
from django.db.models import CharField

# Create your models here.

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
  
    def __str__(self):
        return self.name

class Song (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 100, null=False, blank=False)
    author = models.CharField(max_length= 50, null=False, blank=False)
    key = models.CharField(max_length= 5, null=False, blank=False)
    ytlink = models.CharField(max_length= 100, null=False, blank=False)
    bpm = models.IntegerField()
    have_track = models.BooleanField()
    tracklink = models.CharField(max_length= 100, null=True, blank=True)

    def __str__(self):
        return self.title

class SongCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.id
