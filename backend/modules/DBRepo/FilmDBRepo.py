from typing import List

from django.core.exceptions import ObjectDoesNotExist

from app.models.Film import FilmORM
from django.db.models import Count, Q

from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.entities.Film import Film


class FilmDBRepo:
    @staticmethod
    def decode_orm_film(orm_film) -> Film:
        genres = []
        for g in orm_film.genres.all():
            genres.append(GenreDBRepo.decode_orm_genre(g))

        actors = []
        for a in orm_film.actors.all():
            actors.append(ActorDBRepo.decode_orm_actor(a))

        countries = []
        for g in orm_film.countries.all():
            countries.append(CountryDBRepo.decode_orm_country(g))

        return Film(title=orm_film.title,
                    year=orm_film.year,
                    description=orm_film.description,
                    id=orm_film.id,
                    genres=genres,
                    actors=actors,
                    countries=countries,
                    image=orm_film.image,
                    created=orm_film.created_at,
                    rating=orm_film.rating,
                    )

    @staticmethod
    def get(film_id):
        try:
            orm_film = FilmORM.objects.get(id=film_id)
            return FilmDBRepo.decode_orm_film(orm_film)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def _sort_films(orm_films, sort='title'):
        if sort == 'date':
            return orm_films.order_by('-created_at')
        elif sort == 'rating':
            return orm_films.order_by("-rating")
        elif sort == 'comment':
            return orm_films.annotate(count=Count('commentorm')).order_by('-count')
        else:
            return orm_films.order_by("title")

    @staticmethod
    def get_all(paramsdict: dict) -> List[Film]:
        orm_films = FilmORM.objects.all()
        orm_films = FilmDBRepo._sort_films(orm_films, paramsdict.get('sort', ['title'])[0])

        params = ['q', 'genre', 'country', 'actor', 'year_from', 'year_to']
        for p in params:
            item = paramsdict.get(p, [])
            if len(item) == 1:
                if p == 'q' and item[0] != '':
                    orm_films = orm_films.filter(
                        Q(title__icontains=item[0])
                    )
                if p == 'year_from' and item[0] != '':
                    orm_films = orm_films.filter(year__gte=item[0])
                elif p == 'year_to' and item[0] != '':
                    orm_films = orm_films.filter(year__lte=item[0])
            if len(item) >= 1:
                if p == 'genre':
                    orm_films = orm_films.filter(genres__id__in=item)
                elif p == 'country':
                    orm_films = orm_films.filter(countries__id__in=item)
                elif p == 'actor':
                    orm_films = orm_films.filter(actors__id__in=item)

        offset = paramsdict.get('offset', [0])[0]
        limit = paramsdict.get('limit', [10])[0]

        orm_films = orm_films[int(offset): int(offset) + int(limit)]

        films = []
        for orm_film in orm_films:
            films.append(FilmDBRepo.decode_orm_film(orm_film))
        return films

    @staticmethod
    def count_rating(film_id):
        film = FilmORM.objects.get(id=film_id)
        likes = film.likeorm_set.all()
        sum = 0
        for like in likes:
            sum += like.value
        if len(likes) != 0:
            rating = sum / len(likes)
            setattr(film, 'rating', rating)
            film.save(update_fields=['rating'])
