from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:brand_id>/',views.find_brand),
    path('cars/',views.cars),
    path('<int:brand_id>/edit_name/',views.edit_brand_name),
    path('<int:brand_id>/edit_descript/',views.edit_brand_description),
]