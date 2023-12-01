from django.db import models
from applications.Country.models import Country

# Create your models here.
class CountryCode(models.Model):
    CountryCode = models.CharField('CountryCode', max_length=20 )
    class Meta:
        verbose_name = 'CountryCode'
CONTINENT_CHOICES = [
        ('T', 'F'),
      
    ]

        

class CountryLanguage(models.Model):
    Language = models.CharField('Language', max_length=35, null=False)
    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    IsOfficial= models.CharField(max_length=20, choices=CONTINENT_CHOICES)
    Percentage = models.DecimalField('Pecentage', max_digits=4, decimal_places=1, null= False)
    Family = models.CharField('Family', max_length=30, null=False)
    Dialect = models.CharField('Dialect', max_length=30, null=False)
    avatar = models.ImageField(
        upload_to='CountryLanguages', blank=True, null=True)
    
    class Meta:
        verbose_name = 'CountryLanguages'
        verbose_name_plural = 'CountryLanguages'
    def __str__(self):
        return self.Name+' ' + self.Population + ' - ' + str(self.id)