# Generated by Django 3.2.7 on 2021-12-15 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_song_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoriesOfSong',
        ),
    ]
