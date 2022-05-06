from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.contrib import messages
from songs.models import Song, Categories, SongCategory
from songs import forms
from django.views.decorators.csrf import csrf_exempt
from cfcmusic.settings import BASE_DIR

# Create your views here.

def songs_home (request):
    docHtml = open("songs/templates/homesongs.html")
    plt = Template(docHtml.read())
    docHtml.close()
    db = Song.objects.all()
    ctx = Context(db)

    return HttpResponse (plt.render(ctx))

@csrf_exempt
def song_list (request):
    form = forms.SongForm()
    song_list = Song.objects.values('id', 'name', 'author', 'key', 'ytlink', 'bpm', 'have_track', 'tracklink')
    categories = Categories.objects.all()

    print(song_list)
    if (request.method == 'POST'):
        filter_artist = request.POST['artistfilter']
        filter_category = request.POST['categoryfilter']

        if not (song_list):
            messages.error(request, "La lista está vacía")

        if (filter_artist and filter_category == "....."):
            song_list = Song.objects.filter(author__contains=filter_artist)
        elif (not filter_artist and filter_category != "....."):
            category = Categories.objects.get(name=filter_category)
            song_list = Song.objects.filter(category__id=category.id)
        elif (filter_artist and filter_category != "....."):
            category = Categories.objects.get(name=filter_category)
            song_list = Song.objects.filter(author__contains=filter_artist, category__id=category.id)        

    ctx = {
        'form': form,
        'database': song_list,
        'categories': categories
    }
    return render (request, 'listsongs.html', ctx)

@csrf_exempt
def song_add (request):
    form = forms.SongForm()

    if (request.method == 'POST'):
        print(request.POST)
        form = forms.SongForm(request.POST)
        if form.is_valid():
            song_name = form.cleaned_data['name']
            song_author = form.cleaned_data['author']
            song_key = form.cleaned_data['key']
            song_bpm = form.cleaned_data['bpm']
            yt_link = form.cleaned_data['ytlink']
            track_link = form.cleaned_data['tracklink']
            have_track = form.cleaned_data['have_track']
            categories = request.POST.getlist('category')

            already_load = Song.objects.filter(name=song_name, author=song_author, ytlink=yt_link, key=song_key).exists()

            if not already_load:
                song = Song(name=song_name, author=song_author, 
                key=song_key, ytlink=yt_link, bpm=song_bpm, have_track=have_track, tracklink=track_link)
                song.save()
                for category in categories:
                    cat = Categories.objects.get(id=category)
                    song_cat = SongCategory(category=cat, song=song)
                    song_cat.save()

                messages.success(request, f"¡Canción agregada correctamente!")
            else:
                messages.error(request, f"¡La canción ya está agregada!")
        else :
            print (form.errors)
            messages.error(request, f"¡Los datos ingresados no son correctos!")

    categories = Categories.objects.all()
    return render (request, 'addsong.html', {'form': form, 'categories':categories})

@csrf_exempt
def add_category (request):
    form = forms.CategoriesForm()

    if (request.method == 'POST'):
        form = forms.CategoriesForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['name']
            already_loaded = Categories.objects.filter(name=category).exists()
            if not already_loaded:
                category_table = Categories.objects.create(name=category)
                category_table.save()
 
                messages.success(request, f"¡Categoría agregada correctamente!")
            else:
                messages.error(request, f"¡La categoría ya está agregada!")
        else :
            print (form.errors)
            messages.error(request, f"¡Los datos ingresados no son correctos!")

    return render (request, 'addcategory.html', {'form': form})
