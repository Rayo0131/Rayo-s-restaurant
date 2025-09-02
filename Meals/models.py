from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=20)
    email = models.EmailField()
    persons = models.CharField(max_length=10)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
    

