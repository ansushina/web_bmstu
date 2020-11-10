from django.contrib import admin

# Register your models here.

from app.models.Genre import GenreORM

admin.site.register(GenreORM)