# Generated by Django 3.2.7 on 2021-12-13 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20211210_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='description',
        ),
    ]