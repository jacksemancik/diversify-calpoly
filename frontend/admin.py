from django.contrib import admin
from frontend import models
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Content, ContentAdmin)
