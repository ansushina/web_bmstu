import pytest

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.entities.Comment import Comment
from modules.entities.Like import Like
from modules.entities.User import User
from tests.domain.CommentBuilder import CommentMother
from tests.domain.LikeBuilder import LikeMother


def userToDict(user: User):
    return {
        'username': user.username,
        'email': user.email,
        'password': user.password or "1111",
    }


def commentToDict(comment: Comment):
    return {
        'text': comment.text
    }


def likeToDict(like: Like):
    return {
        'value': like.value
    }


# def filmToDict(film: Film):
#     return {
#         'title': film.title,
#         'year': film.year,
#         'description': film.description,
#         'id': film.id,
#         'genres': film.genres,
#         'actors': film.actors,
#         'countries': film.countries,
#         'image': film.image,
#         'created': film.created,
#         'rating': film.rating
#     }
#

class TestAll:
    # @pytest.mark.parametrize('x', range(150))
    @pytest.mark.parametrize('x', range(1))
    def test_all(self, x, films_3, simple_profile, client):
        # arrange
        test_films = [FilmDBRepo.decode_orm_film(films_3[i]) for i in range(len(films_3))]
        test_films_genre_1 = test_films[0].genres[0]
        test_film_with_genre = test_films[0]

        test_profile = UserDBRepo.decode_orm_user_profile(simple_profile)
        test_user = userToDict(test_profile)

        comment_builder = CommentMother.one()
        test_comment = comment_builder.build()
        like_builder = LikeMother.one()
        test_like = like_builder.build()

        # act
        resp = client.post("/api/v1/sessions/", test_user)
        # print(resp.json())

        # assert
        assert resp.json()['username'] == test_user['username']

        session = resp.json()['token']

        # act
        resp = client.get("/api/v1/films/", HTTP_AUTHORIZATION='Bearer ' + session)
        # print(resp.json())
        resp = resp.json()

        # assert
        for i in range(len(test_films)):
            assert test_films[i].id in [resp[i]['id'] for i in range(len(resp))]

        # act
        resp = client.get("/api/v1/films/?genre=" + str(test_films_genre_1.id))
        print(resp.json())
        result_films = resp.json()

        # assert

        for i in range(len(result_films)):
            film_genres_ids = [result_films[i]['genres'][j]['id'] for j in
                               range(len(result_films[i]['genres']))]
            assert test_films_genre_1.id in film_genres_ids

        # act
        resp = client.get("/api/v1/films/" + str(result_films[0]['id']) + '/')

        # assert
        assert test_film_with_genre.id == resp.json()['id']

        # act
        resp = client.get("/api/v1/films/" + str(result_films[0]['id']) + '/comments/')

        # assert
        assert [] == resp.json()

        # act
        resp = client.post("/api/v1/films/" + str(result_films[0]['id']) + '/comments/',
                           commentToDict(test_comment),
                           HTTP_AUTHORIZATION='Bearer ' + session)

        # assert
        assert resp.json()['text'] == test_comment.text

        # act

        resp = client.post("/api/v1/films/" + str(result_films[0]['id']) + '/likes/',
                           likeToDict(test_like),
                           HTTP_AUTHORIZATION='Bearer ' + session)

        # assert
        assert resp.json()['value'] == test_like.value
