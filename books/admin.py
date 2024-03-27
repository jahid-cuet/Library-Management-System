from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Book)
# admin.site.register(models.Category)
admin.site.register(models.Comment)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(models.Category,BrandAdmin)