from django.contrib.auth.models import User
from django.db import models

# Create your models here.

"""
Models: Book, Author, Genre, Translator, Rating, BookGenre, BookTranslator

Book:
    title - CharField
    author - ForeignKey(Author)
    publication_date - DateField
    user - ForeignKey(User)
    number_of_pages - IntegerField
    book_cover - ImageField
    available - BooleanField
    
# It's not specified in the text that we need an author, 
but it's a better way to make the author as a seperate Model
Author: 
    name - CharField
    surname - CharField
    country - CharField
    
Genre:
    name - CharField
    description - TextField
    
Translator:
    name: CharField
    nationality: CharField
    birth_date: DateField
    
Rating:
    user - ForeignKey(User)
    rating - FloatField
    comment - TextField
    
BookGenre:
    book -ForeignKey(Book)
    genre - ForeignKey(Genre)
    
BookTranslator:
    book - ForeignKey(Book)
    translator - ForeignKey(Translator)
"""


class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    number_of_pages = models.IntegerField(default=0)
    book_cover = models.ImageField(upload_to="images/", null=True, blank=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.author}'


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField(default=0)
    comment = models.TextField()

    def __str__(self):
        return f'{self.rating}'


class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.book} - {self.genre}'


class BookTranslator(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.book} - {self.translator}'
