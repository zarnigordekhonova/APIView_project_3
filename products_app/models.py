from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)
    video = models.FileField(upload_to='products_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='products_audio/', blank=True, null=True)
    docx = models.FileField(upload_to='products_files/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"{self.category.name} - {self.name}"
