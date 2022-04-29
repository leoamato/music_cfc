from django import forms
from django.forms import ModelForm
from songs import models

class SongForm (ModelForm):
    class Meta:
        model = models.Song
        fields = ['id',
            'name',
            'author', 
            'key', 
            'ytlink',
            'bpm',
            'have_track',
            'tracklink',
            'category'
        ]

class CategoriesForm (ModelForm):
    class Meta:
        model = models.Categories
        fields = ['id', 'name']

