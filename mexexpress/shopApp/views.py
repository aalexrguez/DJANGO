from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    
    productos = [
        { 
         'name' : 'Relog Citizen',
         'cost' : 150.00,
         'image': 'https://ss376.liverpool.com.mx/xl/1136440248.jpg'
         },
         {
             'name' : 'Peluche de Batman',
             'cost' : 35.00,
             'image': 'https://m.media-amazon.com/images/I/81eU3-uPjWL.jpg'
         },
         {
             'name' : 'Consola de videojuegos Xbox',
             'cost' : 500.00,
             'image': 'https://http2.mlstatic.com/D_Q_NP_942133-MLA74651936102_022024-O.webp'
         },
         {
             'name' : 'RTX 3060',
             'cost' : 350.00,
             'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuwkXO4SLaQaDrbkzzTLErafkmjAPk8fJpIw&s'
         }
    ]
    context = {
        "user" : "Alex",
       "speacial_offers": productos
       
       
    }
    return render(request,'shopApp/index.html',context)

