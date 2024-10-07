from django.contrib import admin
from .models import Book, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model  = Book