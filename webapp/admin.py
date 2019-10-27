from django.contrib import admin
from . models import employees

class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(employees, YourModelAdmin)


# Register your models here.
