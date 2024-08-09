from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventoy

#decorador sendo um receiver(ouve evento que está chegando) - a funcao sera disparada no evento pre save da tabela de carros(model cars) - ou seja, o que for pre save, vai pra funcao

def car_inventory_update():

    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        #aggregate cria campos na query - criando campo total_value na query
        total_value=Sum('value')
    )['total_value']
    CarInventoy.objects.create(
        cars_count=cars_count,
        cars_value= cars_value
    )
  
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance,**kwargs):
    ...
    
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
  
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
    