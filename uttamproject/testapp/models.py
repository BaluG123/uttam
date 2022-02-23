from django.urls import reverse
from statistics import mode
from django.db import models

# Create your models here.
class Work(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('upload','Upload'))
    MONEY_CHOICES = (('given','Given'),('taken','Taken'))
    place=models.CharField(max_length=10000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    Name=models.CharField(max_length=1000)
    about_work=models.CharField(max_length=10000)
    choose=models.CharField(max_length=15,choices=MONEY_CHOICES)
    amount=models.IntegerField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Name    

    def get_absolute_url(self):
        return reverse('home')    

