# Generated by Django 4.0.4 on 2022-04-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0014_alter_categories_options_alter_song_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.CharField(max_length=5),
        ),
    ]
