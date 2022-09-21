from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()

    number_watched = 0
    not_watched = 0
    for item in data_mywatchlist:
        if (item.watched):
            number_watched += 1
        else:
            not_watched += 1
    
    context = {
        "student_nama": "Raditya Aditama",
        "student_id": "2106750313",
        "list": data_mywatchlist ,
        "number_watched": number_watched,
        "not_watched": not_watched
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")