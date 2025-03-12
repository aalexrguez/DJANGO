from django.shortcuts import render
from django.http import HttpResponse 
from .models import Product,Contacts
# Create your views here.
def index(request):
    product_list = Product.objects.all()
    speacial_offers = Product.objects.filter(product_is_offer=True)
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
       "speacial_offers": speacial_offers,
       "product_list":product_list
       
       
    }
    return render(request,'shopApp/index.html',context)

def about(request):
    contacts_list = Contacts.objects.filter(contact_activate=True)
    context = {
        'contacts': contacts_list
    }
    return render(request,'shopApp/about.html',context)