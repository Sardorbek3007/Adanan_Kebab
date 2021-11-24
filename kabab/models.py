from django.db import models

# Create your models here.
class Menyu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField
    content = models.TextField()
    category = models.ForeignKey('Category', related_name="news", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
        name = models.CharField(max_length=300)

        def __str__(self):
            return self.name