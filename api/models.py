from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"


class State(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.name