from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    pass

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Event, EventAdmin)
#admin.site.register(Category, CategoryAdmin)