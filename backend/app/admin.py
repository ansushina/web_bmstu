from django.contrib import admin

# Register your models here.
from app.models.Actor import ActorORM
from app.models.Genre import GenreORM
from app.models.Country import CountryORM
from app.models.Profile import ProfileORM

admin.site.register(GenreORM)
admin.site.register(CountryORM)
admin.site.register(ActorORM)
admin.site.register(ProfileORM)