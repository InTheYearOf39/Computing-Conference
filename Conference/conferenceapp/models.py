from django.db import models

# Create your models here.
class Registrationform (models.Model):
    
    name           = models.CharField(max_length=100, blank=True)
    email          = models.CharField(max_length = 100, blank = True)
    district       = models.CharField(max_length = 100, blank = True)
    profession     = models.CharField(max_length = 100, blank = True)
    
    
    

    def __str__ (self):
        return self.name

class Program(models.Model): 
    name = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    speaker = models.ForeignKey(Registrationform,on_delete=models.CASCADE)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name