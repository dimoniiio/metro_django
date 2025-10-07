from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка поста."""

    list_display = ('title', 'content_preview')
    search_fields = ('title', 'content')
    fields = ('title', 'content')
    list_per_page = 20

    def content_preview(self, obj):
        return (obj.content[:100] + '...'
                if len(obj.content) > 100 else obj.content)
    content_preview.short_description = 'Содержание (предпросмотр)'
