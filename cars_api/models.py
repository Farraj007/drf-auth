from django.db import models
from django.contrib.auth import get_user_model

class Cars(models.Model):
    Car_Type=(
        ('Sedan','Sedan'),
        ('SUV','SUV'),
        ('Coupe','Coupe'),
        ('Hatchback','Hatchback'),
        ('Convertible','Convertible'),
        ('Crossover','Crossover'),
        ('Truck','Truck'),
        ('Van','Van'),
        ('Wagon','Wagon'),
        ('Other','Other'),
    )
    Manufacturer = models.CharField(max_length=255)
    Type=models.CharField(max_length=13, choices=Car_Type)
    Model = models.CharField(max_length=100)
    Specs = models.TextField()
    Seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE )
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateField()
    # class Meta:
    #     app_label = 'cars_api'
    def __str__(self):
        return self.Manufacturer