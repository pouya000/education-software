from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name']
    class Meta:
        model = models.User
admin.site.register(models.User,UserAdmin)
# admin.site.register(models.User)


