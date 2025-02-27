from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    
    productos = [
        { 
         'name' : 'Relog Citizen',
         'cost' : 150.00
         },
         {
             'name' : 'Peluche de Batman',
             'cost' : 35.00
         },
         {
             'name' : 'Consola de videojuegos Xbox',
             'cost' : 500.00
         }
    ]
    context = {
        "user" : "Alex",
       "speacial_offers": productos
       
       
    }
    return render(request,'shopApp/index.html',context)

