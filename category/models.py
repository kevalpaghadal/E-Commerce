from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    category_slug = models.CharField(max_length=100, unique=True)
    category_description = models.TextField( blank=True , null=True)
    category_image = models.ImageField(upload_to= "photos/category" , blank=True , null=True)

    class Meta:   # change name for modul in admin penal
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse('products_by_category' , args=[self.category_slug])

    def __str__(self):
        return self.category_name