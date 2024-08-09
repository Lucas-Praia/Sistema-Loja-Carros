from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView


#Pra ser uma ListView tem que ser Get. Por isso ele entende automaticamente.
class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'  
    
#get_queryset() - entende que vai pegar a car.objects.all e ordena pelo model
#bloco que faz a busca do usuario pelo carro
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
        
        
@method_decorator(login_required(login_url='login'), name='dispatch')
#dispatch verifica alguns dados basicos como get ele faz uma coisa, post #faz outra, se tem body na requisicao)
class NewCarCreateView(CreateView): #Isso é o equivalente o codigo de cima, django entende automaticamente usando os conceitos de herança da createview.
    
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy ('car_detail', kwargs={'pk': self.object.pk})
    
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

