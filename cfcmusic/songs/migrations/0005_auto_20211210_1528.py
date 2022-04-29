# Generated by Django 3.2.7 on 2021-12-10 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20210430_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='description',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CategoriesOfSong',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.categories')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.song')),
            ],
        ),
    ]
