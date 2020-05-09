from django.contrib import admin
from django.utils.text import slugify
from django.utils import timezone
# Register your models here.

from .models import Post
from .models import Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','slug','pub_date','was_published_recently')
admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_text',)}
    list_display = ('category_text','slug')
admin.site.register(Category,CategoryAdmin)



