from django.contrib import admin
from django.urls import path
from .views import HomePageView ,carsListView ,carDetailsView ,carCreateView ,carUpdateView, carDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cars', carsListView.as_view(), name='cars_list'),
    path('<int:pk>', carDetailsView.as_view(), name="car_details"),
    path('create', carCreateView.as_view(), name='create_car'),
    path('update/<int:pk>', carUpdateView.as_view(), name="car_update"),
    path('delete/<int:pk>', carDeleteView.as_view(), name="car_delete")
]