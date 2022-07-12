import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Brand, Car
from django.views.decorators.csrf import csrf_exempt


def get_brand(brand_id):
    brand= Brand.objects.get(id=brand_id)
    return brand

def index(request):
    brands=Brand.objects.all()
    return render(request,'cars_and_brands/index.html', {"brands":brands})

def cars(request):
    cars=Car.objects.all()
    return render(request,'cars_and_brands/cars.html', {"cars":cars})

def find_brand(request,brand_id):
    brand= get_brand(brand_id)
    return render(request,'cars_and_brands/brand.html', {"brand":brand})

@csrf_exempt
def edit_brand_name(request, brand_id):
    # Should be request.method
    if request.method == 'POST':
        body = json.loads(request.body) 
        brand_id = body['brand_id']
        brand=get_brand(brand_id)
        new_name= body['new_name']
        # Can't use this if it's just the name, add new description variable
        # new_description=body['new_description']
        if new_name:
            brand.name=new_name
            brand.save()
            return  JsonResponse({'brand_id': brand_id, 'brand_name':new_name})
    # MUST return some sort of response
    return JsonResponse({'brand_id': "FAILED", 'brand_name':"FAILED", "brand_description": "FAILED"})

@csrf_exempt
def edit_brand_description(request, brand_id):
    # Should be request.method
    if request.method == 'POST':
        body = json.loads(request.body) 
        brand_id = body['brand_id']
        brand=get_brand(brand_id)
        # Can't use this if it's just the name, add new description variable
        new_description=body['new_description']
        brand.description= new_description
            # Save changes
        brand.save()
        return  JsonResponse({'brand_id': brand_id, 'brand_name':brand.name, "brand_description": new_description})
    # MUST return some sort of response
    return JsonResponse({'brand_id': "FAILED", 'brand_name':"FAILED", "brand_description": "FAILED"})

# create virtual environment
# source ~/VEnvirons/Validation_Practice_VE/bin/activate
# create database (psql postgres -> create database dbname->\q-> psql dbname)
# connect database in project settings file.
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'amazon',
    #     }
    # }
# add app name to settings installed_apps
# python manage.py makemigrations <appname>
# python manage.py migrate
# \dt  inside database should now show you the tables you've created
# python manage.py test