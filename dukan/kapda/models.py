from django.db import models

class ProductCard (models.Model) :

    CATEGORIES = [
        ('Mens' , 'Mens'),
        ('Ladies', 'Ladies'),
    ]

    CURRENCY = [
        ('$', 'USD'),
        ('रु', 'NRP'),
    ]

    SIZE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    image = models.ImageField(upload_to = 'productsimg/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Enter the URL of the image.")
    description = models.CharField(max_length = 300)
    size = models.CharField(choices = SIZE, max_length = 6)
    categories = models.CharField(choices = CATEGORIES, max_length = 6)
    currency = models.CharField(choices = CURRENCY, max_length = 3, default = '$')
    price = models.IntegerField()

    def __str__ (self) :
        return f"{self.description [:25]} - {self.categories} - {self.currency} - {self.price}"
