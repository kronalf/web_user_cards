from django.contrib import admin
from .models import Person, Department, Floor

# Register your models here.

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Floor)

