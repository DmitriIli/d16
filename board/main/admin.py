from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Categories)
admin.site.register(Ads)
admin.site.register(FeedBack)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)