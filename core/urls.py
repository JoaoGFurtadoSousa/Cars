"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars.views import view_cars,search_car_by_url, create_new_car, put_car, create_car_w_forms
from django.conf.urls.static import static, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', search_car_by_url, name = 'search_car_by_url'),
    path('create/', create_new_car, name = 'create_new_car'),
    path('att/', put_car, name = 'put_car'),
    path('create_with_forms/',create_car_w_forms, name = 'criar_carro_com_form'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
