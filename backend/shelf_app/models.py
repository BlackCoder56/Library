from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=60)
    
    def __str__(self):
        return self.categoryName
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    total = models.PositiveIntegerField()
    # # borrowed = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.title