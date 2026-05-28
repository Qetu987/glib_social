from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'is_active', 'is_visible', 'date')
    search_fields = ('id', 'title', 'owner')
    list_filter = ('is_active', 'is_visible', 'date')
    list_editable = ('is_active', 'is_visible')
    ordering = ('-date',)
    list_per_page = 25