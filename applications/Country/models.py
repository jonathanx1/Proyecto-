from django.db import models
class Continent(models.TextChoices):
        Asia='Asia', 
        Europe='Europe',
        Africa='Africa', 
        Antartica= 'Antartica',
        Oceania= 'Oceania',
        North_America='North America', 
        South_America='South America',
        
    

class Country(models.Model):
    Code = models.CharField('Code', max_length=3, null=False, primary_key=True)
    Name = models.CharField('Name', max_length=52, null=False)
    continent = models.CharField(max_length=20, choices=Continent.choices)
    Region = models.CharField('Region', max_length=26, null=False)
    SurfaceArea = models.DecimalField('SurfaceArea',max_digits=10.2,decimal_places=2, null=False )
    IndepYear = models.SmallIntegerField('IndepYear', max_length=10, null=False)
    Population = models.IntegerField('Population', max_length=20, null= False)
    LifeExpentacy = models.DecimalField('LifeExpentacy',max_digits=3, decimal_places=1, null=False)
    GNP= models.DecimalField('GNP',  max_digits= 10, decimal_places=2, null= False)
    GNPOld = models.DecimalField('GNPOld', max_digits=10, decimal_places=2, null=False)
    LocalName = models.CharField('LocalName',max_length=45, null=False)
    GovermentForm = models.CharField('GovermentForm',max_length=45, null=False)
    HeadOfState = models.CharField('HeadOfState',max_length=60, null=False)
    Capital = models.IntegerField('Capital',max_length=5, null=False)
    Code2 = models.CharField('Code2',max_length=2, null=False)
    Money = models.CharField('Money',max_length=30, null=False)
    IDH = models.DecimalField('IDH',max_digits=10, decimal_places=2, null=False)
    search_fields = ('Code', 'Name',)
    list_filter = ('NameCountry',)
    class Meta:
            verbose_name = 'Code'
            verbose_name_plural = 'Codes Country'
            ordering = ['Name']
            unique_together = ('Code', 'Name')
    def __str__(self):
        return self.Code + ' - ' + self.Name + str(self.id)

