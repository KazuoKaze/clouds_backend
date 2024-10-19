from django.db import models
from product.models import Product
from .make_slug_from_name import make_slug_from_name
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Category'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        if self.name:
            get_slug_name = make_slug_from_name(self.name)
            self.slug = get_slug_name
            super().save()


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True)
    product = models.ManyToManyField(Product, related_name='product', blank=True)
    slug = models.SlugField(blank=True, null=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'SubCategory'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        if self.name:
            get_slug_name = make_slug_from_name(self.name)
            self.slug = get_slug_name
            super().save()


@receiver(post_save, sender=Category)
def make_custom_sub_category(sender, instance, created, **kwargs):
    if created:
        SubCategory.objects.create(name=f'All {instance.name}', category=instance)