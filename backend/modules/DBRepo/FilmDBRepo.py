from app.models.Film import FilmORM
from django.db.models import Count, Q
from modules.entities.Film import Film

class FilmDBRepo:
    def _decode_ORM(self, orm_film):
        entity = Film(title=orm_film.title,
                      year=orm_film.year,
                      description=orm_film.description,
                      id=orm_film.id,
                      genres=orm_film.genres,
                      actors=orm_film.actors,
                      countries=orm_film.countries,
                      image=orm_film.image,
                      created=orm_film.created_at,
                      comments=orm_film.comment_set.all(),
                      rating=orm_film.rating,
                      )

    def get(self, id):
        orm_film = FilmORM.objects.get(id=id)
        # parse film to entity
        return self._decode_ORM(orm_film)

    def new_top(self):
        return Film.objects.order_by('-created_at')[:10]

    def most_commented(self):
        return Film.objects.annotate(count=Count('comment')).order_by('-count')[:10]

    def most_rating(self):
        return Film.objects.order_by('-rating')[:10]

    def count_rating(self, film_id):
        film = Film.objects.get(id=film_id)
        likes = film.like_set.all()
        sum = 0
        for like in likes:
            sum += like.value
        if len(likes) != 0:
            rating = sum / len(likes)
            setattr(film, 'rating', rating)
            film.save(update_fields=['rating'])

    def search_with_filters(self, querydict):
        films = Film.objects.all()
        params = ['q', 'genre', 'country', 'actor', 'year_from', 'year_to']
        for p in params:
            item = querydict.getlist(p)
            if len(item) == 1:
                if p == 'q' and item[0] != '':
                    films = films.filter(
                        Q(title__icontains=item[0])
                    )
                if p == 'year_from' and item[0] != '':
                    films = films.filter(year__gte=item[0])
                elif p == 'year_to' and item[0] != '':
                    films = films.filter(year__lte=item[0])
            if len(item) >= 1:
                if p == 'genre':
                    films = films.filter(genres__id__in=item)
                elif p == 'country':
                    films = films.filter(countries__id__in=item)
                elif p == 'actor':
                    films = films.filter(actors__id__in=item)
        return films

