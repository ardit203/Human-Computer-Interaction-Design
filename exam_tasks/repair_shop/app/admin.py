from django.contrib import admin
from .models import *


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['car_type', 'max_speed']


class RepairAdmin(admin.ModelAdmin):
    exclude = ['user', ]

    def save_model(self, request, obj, form, change):
        if obj:
            obj.user = request.user
            super(RepairAdmin, self).save_model(request, obj, form, change)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_add_permission(self, request):
        return request.user.is_superuser


class WorkshopManufacturerInline(admin.StackedInline):
    model = WorkshopManufacturer
    extra = 0


class WorkshopAdmin(admin.ModelAdmin):
    inlines = [WorkshopManufacturerInline, ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Repair, RepairAdmin)
