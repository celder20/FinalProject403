from django.db import models

# Create your models here.
class footballlingo(models.Model) :
    lingoid = models.AutoField(primary_key=True)
    term = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return (self.term)