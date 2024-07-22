from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class Car(models.Model):
    model = models.CharField(max_length=100, blank=False, null=False)  # required
    brand = models.CharField(max_length=100, blank=False, null=False)  # required
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)  # required
    is_bought = models.BooleanField(blank=False, null=False)  # required
    buyer_id = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete= models.CASCADE)  # not required
    buy_time = models.DateTimeField(default=timezone.now ,null=True, blank=True)  # not required

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    def get_absolute_url(self):
        return reverse('car_details', args=[self.id])
