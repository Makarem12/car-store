from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class carsListView(ListView):
    template_name='carsList.html'
    model= Car
    template_name = "cars_list.html"
    context_object_name = "cars_objs"    

class carDetailsView(DetailView):
    model = Car
    template_name = "car_details.html"    

class carCreateView(CreateView):
    model=Car
    template_name = 'car_create.html'
    fields = ['model', 'brand', 'price', 'is_bought', 'buyer_id', 'buy_time']    

class carUpdateView(UpdateView):
     model = Car
     template_name= 'car_update.html'
     fields = "__all__"    

class carDeleteView(DeleteView):
    model=Car
    template_name='car_delete.html'
    success_url = reverse_lazy('cars_list') 