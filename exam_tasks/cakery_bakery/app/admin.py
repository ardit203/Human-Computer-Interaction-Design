from django.contrib import admin
from django.db.models import Count

from .models import *


# Register your models here.


class BakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(BakerAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs.annotate(cakes_count=Count('cakes')).filter(cakes_count__lt=5)

        return qs


class CakeAdmin(admin.ModelAdmin):
    list_display = ['name', ]

    def has_change_permission(self, request, obj=None):
        return obj and request.user == obj.baker.user

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user=request.user).first()

        cakes = Cake.objects.filter(baker=baker)

        if not change and len(cakes) > 10:
            return

        sum = 0

        for cake in cakes:
            sum += cake.price

        if not change and sum + obj.price > 10000:
            return

        old_cake = Cake.objects.filter(id=obj.id)

        if change and sum + obj.price - old_cake.price > 10000:
            return

        if obj and Cake.objects.filter(name=obj.name).exists():
            return

        super(CakeAdmin, self).save_model(request, obj, form, change)


admin.site.register(Cake, CakeAdmin)
admin.site.register(Baker, BakerAdmin)
