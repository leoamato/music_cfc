from django.shortcuts import render
import calendar
import datetime

# Create your views here.

def mark_today (htmlfile, day):
    index = htmlfile.index(str(day))

    textToAdd = 'style="color:rgb(350, 90, 0);"'
    htmlfile = htmlfile[:index-1] + " " + textToAdd + htmlfile[index-1:]

    return htmlfile

def home_sched (request):
    date = datetime.datetime.now()
    weekindex = date.weekday()

    day = date.day
    month = date.month
    year = date.year

    c = calendar.HTMLCalendar(calendar.SUNDAY)
    cal = c.formatmonth(year, month)
    cal = mark_today(cal, day)

    ctx = {
        "year": year,
        "calendar": cal,
    }

    return render (request, 'homesched.html', ctx)