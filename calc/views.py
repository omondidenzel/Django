from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {"name":"Denzel"})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, "result.html", {'result':res} )

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The city that never sleeps"
    dest1.img = "destination_1.jpg"
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderbad'
    dest2.desc = "First Biryani, Then Sherwani"
    dest2.img = "destination_2.jpg"
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = "Beautiful city"
    dest3.img = "destination_3.jpg"
    dest3.price = 750
    dest3.offer = False
    
    dests = [dest1, dest2, dest3]

    dest = Destination.objects.all()

    return render(request, "index.html", {'dest1': dest})