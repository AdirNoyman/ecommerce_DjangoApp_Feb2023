from django.db import models

# Create your models here.


class Category(models.Model):
    # We index the category name so the DB querys will be more efficent
    name = models.CharField(max_length=250, db_index=True)
    # The category URL enpoint
    slug = models.SlugField(max_length=250, unique=True)

    # set how the plural of Category plural name, explictly, for the admin
    class Meta:
        verbose_name_plural = 'categories'
    # Set the tostring name of the Category name

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    # 'TextField' - enables entering more text. and we want to set to optional so that wy we have set it to 'blank=True'
    description = models.TextField(blank=True)
    # The product URL enpoint
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    # set how the plural of Category plural name, explictly, for the admin

    class Meta:
        verbose_name_plural = 'products'
    # Set the tostring title of the Product name

    def __str__(self):
        return self.title
