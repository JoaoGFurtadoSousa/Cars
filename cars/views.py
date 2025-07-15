from django.shortcuts import render
from .models import Cars
# Create your views here.

def view_cars(request):
        cars = Cars.objects.all()
        return render(request, 'index.html', {'cars': cars})
    
