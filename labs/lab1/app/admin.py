from django.contrib import admin
from .models import *
# Register your models here.

""""
The user who adds a book is automatically assigned as its owner based on the logged-in user,
and only that user can edit or delete the book.
Books should be filterable based on their availability for reading.

"""


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'user']
    list_filter = ['available', ]
    exclude = ['user', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


""""
where adding and deleting Genres is only allowed for superusers.

"""


class GenreAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'nationality']


""""
only the user who left the rating can delete it.
Which also applies that the user that adds the rating is assigned as the user

"""


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating', 'comment', 'user']
    exclude = ['user', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RatingAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj:
            return request.user == obj.user
        return False


class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['book', 'genre']


class BookTranslatorAdmin(admin.ModelAdmin):
    list_display = ['book', 'translator']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(BookTranslator, BookTranslatorAdmin)
