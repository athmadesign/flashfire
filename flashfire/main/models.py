from django.db import models
from django.utils.text import slugify

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    trending = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.product.name} - {self.name or 'Image'}"
