from django.db import models
from category.make_slug_from_name import make_slug_from_name

# Create your models here.

class ProductSize(models.Model):
    """Represents available sizes (like Small, Medium, Large)."""
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Product Sizes'
        ordering = ['-timestamp']


class AddImages(models.Model):
    """Represents images linked to a specific product."""
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images', null=True)  
    image = models.ImageField(upload_to='uploads/', null=True) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Product(models.Model):
    """Represents the main product (like a shirt)."""
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        if self.name:
            get_slug_name = make_slug_from_name(self.name)
            self.slug = get_slug_name
            super().save()



class ProductVariant(models.Model):
    """Represents a specific variant of a product (e.g., Shirt - Medium) with its own price."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='variants')
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.PositiveIntegerField(default=0)  
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.size.name}"
    
    class Meta:
        verbose_name_plural = 'Product Variants'
        ordering = ['-timestamp']
