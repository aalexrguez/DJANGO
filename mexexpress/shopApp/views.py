from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    
    entrenadores = [
        'Joel Marquez',
        'Alonso Quintana',
        'Omar Chavez'
    ]
    Horario = [
        '8:00 - 9:00',
        '10:00 - 12:00'
    ]
    clientes = [
        'Alex Rodriguez',
        'Andres Ramos',
        'Cristian Villa'
    ]
    context = {
       "entrenador":entrenadores,
       "horario":Horario,
       "clientes":clientes
    }
    return render(request,'shopApp/index.html',context)

