from django.db import models
from applications.Country.models import Country

# Create your models here.
class CountryCode(models.Model):
    CountryCode  = models.CharField('CountryCode ', max_length=30)
    class Meta:
        verbose_name = 'CountryCode '

        

class City(models.Model):
    ID = models.IntegerField('ID', max_length=30, primary_key=True)
    Name = models.CharField('Name', max_length=35, null=False)
    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    District = models.CharField('District', max_length=20, null= False)
    Population = models.IntegerField('Population', max_length= 20, null= False)
    Mayor = models.CharField('Mayor', max_length=30, null=False) 
    avatar = models.ImageField(
        upload_to='Citys', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Name City'
        verbose_name_plural = 'Names Citys'


    def __str__(self):
        return self.Name+' ' + self.Population + ' - ' + str(self.id)