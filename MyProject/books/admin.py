from django.contrib import admin
from .models import Book
from books.models import Comment
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','publisher')
    list_display_links=('id','book_name')
    list_filter=('author',)
    search_fields=('book_name','author','publisher','category','price','page_number')
    list_per_page=20

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    search_fields = ('subject','comment','ip','user','books','rate','id')
    list_per_page=20


admin.site.register(Book,BookAdmin)
admin.site.register(Comment,CommentAdmin)