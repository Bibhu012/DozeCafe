from django.shortcuts import render
from .models import coffee_section_2 
# Create your views here.

def index(request): 
    #return render(request, "index.html")
    #return render(request, "index.html",{'price':70})
    
    

   ''' coffee1 = coffee_section_2()
    coffee1.name = 'CAPPUCCINO'
    coffee1.desc = 'Nice Coffee'
    coffee1.img = 'img-1.png'
    coffee1.price = 55
    coffee1.offer = False

    
    coffee2 = coffee_section_2()
    coffee2.name = 'BEAN VARIETIES'
    coffee2.desc = 'Description 2'
    coffee2.img = 'img-2.png'
    coffee2.price = 65
    coffee2.offer = True

    
    coffee3 = coffee_section_2()
    coffee3.name = 'COFFEE & PASTRY'
    coffee3.desc = 'Description 3'
    coffee3.img = 'img-3.png'
    coffee3.price = 75
    coffee3.offer = False

    
    coffee4 = coffee_section_2()
    coffee4.name = 'COFFEE TO GO'
    coffee4.desc = 'Description 4'
    coffee4.img = 'img-4.png'
    coffee4.price = 85
    coffee4.offer = True 

    coffee = [coffee1, coffee2, coffee3, coffee4] '''

   return render(request, "index.html",{'coffee': coffee})
coffee = coffee_section_2.objects.all()

    #return render(request, "index.html",{'coffee1' : coffee1, 'coffee2' : coffee2, 'coffee3' : coffee3, 'coffee4' : coffee4})
