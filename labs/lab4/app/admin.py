from django.contrib import admin
from .models import *

# Register your models here.

""""
Display cars by their name and type.
The logged-in user that adds the car gets assigned as its user.
Only the user who adds the car and a superuser can delete the car
You should enable filtering cars by type

Manufacturers can only be added and deleted by superusers
Manufacturers should be displayed by their name and owner
Users can only see manufacturers that manufacture cars that they own
"""


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    exclude = ['user', ]
    list_filter = ['type']

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        return super(CarAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return obj and (request.user == obj.user or request.user.is_superuser)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        # "car" is the reverse relation of the ForeignKey Car.manufacturer.
        # car__user=request.user -> means “find all manufacturers where at least
        # one of their cars was added by this user.”
        return Manufacturer.objects.filter(car__user=request.user).distinct()


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
