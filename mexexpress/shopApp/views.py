from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    
    productos = [
        'Reloj Citizen',
        'Playera del Barcelona',
        'Crema para piel'
    ]
    context = {
       "products":productos,
       
    }
    return render(request,'shopApp/index.html',context)

