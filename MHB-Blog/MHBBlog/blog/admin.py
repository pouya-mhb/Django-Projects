from django.contrib import admin
from blog.models import Post

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author' , 'publish_date' , 'status' , 'slug'
    ]

    list_filter = [
        'title' , 'status' , 'publish_date'  , 'created_date'
    ]

    search_fields = [
        'title' , 'status' , 'publish_date'  , 'created_date'
    ]

    prepopulated_fields = {
        'slug' : ('title','author') # i love this one
    }

    raw_id_fields = ('author',)

    date_hierarchy = 'publish_date'

    ordering = (
        'author' , 'publish_date' , 'status'
    )