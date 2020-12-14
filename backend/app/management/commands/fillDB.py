import os

import requests

from app.models.Actor import ActorORM
from app.models.Country import CountryORM
from app.models.Film import FilmORM
from app.models.Genre import GenreORM
from database.parser import Parser
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.db import transaction

parser = Parser();


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    @transaction.atomic()
    def handle(self, *args, **options):

        self.generate_genres()
        self.generate_countries()
        self.generate_actors()
        self.generate_films()
        self.set_images()

    def generate_genres(self):
        genres = parser.get_genres()
        print("GENERATE_GENRES ", len(genres))
        for g in genres:
            GenreORM.objects.create(
                name=g,
            )

    def generate_countries(self):
        countries = parser.get_countries()
        print("GENERATE_COUNTRIES ", len(countries))
        for c in countries:
            CountryORM.objects.create(
                name=c,
            )

    def generate_actors(self):
        actors = parser.get_actors()
        print("GENERATE_ACTORS ", len(actors))
        for actor in actors:
            ActorORM.objects.create(
                firstName=actor['first_name'],
                lastName=actor['last_name'],
            )

    def generate_films(self):
        films = parser.get_films()
        print("GENERATE_FILMS ", len(films))
        genres = GenreORM.objects.all()
        genres_id = list(GenreORM.objects.values_list('id', flat=True))
        actors = ActorORM.objects.all()
        countries = CountryORM.objects.all()
        for film in films:
            f = FilmORM.objects.create(
                title=film['title'],
                year=film['year'],
                description=film['description']
            )
            f.save()
            for g in film['genres']:
                for genre in genres:
                    if genre.name == g:
                        f.genres.add(genre.id)
            for g in film['actors']:
                for actor in actors:
                    if actor.firstName == g['first_name'] and actor.lastName == g['last_name']:
                        f.actors.add(actor.id)
            for g in film['countries']:
                for country in countries:
                    if country.name == g:
                        f.countries.add(country.id)
            print(films.index(film))

    def set_images(self):
        films = parser.get_films()
        for film in films:
            r = requests.get(film['image'])
            film_ob = FilmORM.objects.filter(title=film['title']).first()

            name = film['image'].split('/')[5]
            print(name)
            f = open(name, "wb+")
            f.write(r.content)

            djangofile = ImageFile(f)
            film_ob.image.save('new', djangofile)
            f.close()

            os.remove(name)
