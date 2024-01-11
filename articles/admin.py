from django.contrib import admin
from .models import Artiicle, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
admin.site.register(Artiicle, ArticleAdmin)
admin.site.register(Comment)
