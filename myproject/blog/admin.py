from django.contrib import admin

# Register your models here.
from .models import Category,Post,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)