from django.shortcuts import render
from .models import Cars
from django.http import HttpResponse
from .forms import FormsCar
# Create your views here.

def view_cars(request):
        cars = Cars.objects.all()
        return render(request, 'index.html', {'cars': cars})

def search_car_by_url(request):
        print(request.method)
        if request.method=='GET':
                search_car = request.GET.get('carro_buscado')
                print(request.GET)
                print(search_car)

                if search_car:
                        data = Cars.objects.filter(brand__icontains = search_car)
                        if len(data)==0:
                                return HttpResponse('NO RESULTS IN DATABASE')
                        return render(request,'index.html',{'cars':data})
        
                else:
                        data = Cars.objects.all()
                        return render(request,'index.html',{'cars':data})
        elif request=='PUT':
                model = request.PUT.get['model']
                print(request.PUT)
                print(model)
                car_in_db = Cars.objects.get(model = model)
                

       

def create_new_car(request):
        if request.method=='GET':
                return render(request,'create_new_car.html')

        elif request.method=='POST':
                model = request.POST.get('model')
                brand = request.POST.get('brand')
                year = request.POST.get('year')
                image = request.FILES.get('image')

                new_car = Cars.objects.create(model = model,
                brand = brand,
                year = year,
                image = image)

                return render(request,'create_new_car.html')

def put_car(request):
        if request.method=='PUT':
                model = request.PUT.get['model']
                car_in_database = Cars.objects.get(model = model)
                print(model)
                print(request.PUT)

        return render(request, 'att_car.html')

def create_car_w_forms(request):
        form = FormsCar()
        model = request.POST.get('model')
        year = request.POST['year']

        new_car = Cars.objects.create(model = model, year = year)
        return render(request, 'forms.html', {'create_car_w_forms':form})


        
                