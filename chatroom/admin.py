from django.contrib import admin
from .models import Chat, Category

class ChatAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatAdmin)
admin.site.register(Category, CategoryAdmin)