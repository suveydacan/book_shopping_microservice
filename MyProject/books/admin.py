from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','publisher')
    list_display_links=('id','book_name')
    list_filter=('author',)
    search_fields=('book_name','author','publisher','category','price','page_number')
    list_per_page=20


admin.site.register(Book,BookAdmin)