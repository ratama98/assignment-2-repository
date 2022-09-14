from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    
    context = {
        "student_nama": "Raditya Aditama",
        "student_id": "2106750313",
        "list": data_katalog
    }

    return render(request, "katalog.html", context)
