import pytest
import pytest_bdd

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.UserDBRepo import UserDBRepo
from tests.app.e2e.test_all import userToDict


@pytest.mark.parametrize('given_text', ['blabla', 'аываыв'])
@pytest.mark.parametrize('given_value', [3, 4, 5])
@pytest_bdd.scenario('working.feature', 'Film evaluating scenario')
def test_film_evaluate(given_text, given_value):
    pass


@pytest_bdd.given('I have user', target_fixture='user')
def user(simple_profile):
    test_profile = UserDBRepo.decode_orm_user_profile(simple_profile)
    test_user = userToDict(test_profile)
    return test_user


@pytest_bdd.given('I have films in database', target_fixture='films')
def films(films_3):
    test_films = [FilmDBRepo.decode_orm_film(films_3[i]) for i in range(len(films_3))]
    return test_films


@pytest_bdd.given('I have context', target_fixture='context')
def context():
    return {}


@pytest_bdd.when('I make login request')
def login(user, client, context):
    resp = client.post("/api/v1/sessions/", user)

    context['resp'] = resp.json()
    user['session'] = resp.json()['token']


@pytest_bdd.then('I am logged in')
def user_logged_in(user, context):
    assert context['resp']['username'] == user['username']


@pytest_bdd.when('I make film request')
def get_films(context, client):
    resp = client.get("/api/v1/films/")

    context['resp'] = resp.json()


@pytest_bdd.then('I have films')
def user_got_films(films, context):
    resp = context['resp']
    for i in range(len(films)):
        assert films[i].id in [resp[i]['id'] for i in range(len(resp))]


@pytest_bdd.when('I make film searching by given_genre request')
def get_films_by_genre(context, client, films):
    genre = films[0].genres[0].id
    resp = client.get("/api/v1/films/?genre=" + str(genre))

    context['genre'] = genre
    context['resp'] = resp.json()
    context['genred_films'] = resp.json()


@pytest_bdd.then('I have searched films')
def user_got_films_by_genre(context):
    result_films = context['resp']
    genre = context['genre']
    for i in range(len(result_films)):
        assert genre in [result_films[i]['genres'][j]['id'] for j in
                         range(len(result_films[i]['genres']))]


@pytest_bdd.when('I make one film with genre request')
def get_films_by_genre(context, client):
    genred_films = context['genred_films']
    resp = client.get("/api/v1/films/" + str(genred_films[0]['id']) + '/')

    context['resp'] = resp.json()


@pytest_bdd.then('I have one film with genre data')
def user_got_films_by_genre(context):
    result_film = context['resp']
    genred_films = context['genred_films']
    genre = context['genre']

    assert result_film['id'] == genred_films[0]['id']
    assert genre in [result_film['genres'][i]['id'] for i in range(len(result_film['genres']))]


@pytest_bdd.when('I make film comments request')
def get_comments(context, client):
    genred_films = context['genred_films']
    resp = client.get("/api/v1/films/" + str(genred_films[0]['id']) + '/comments/')

    context['resp'] = resp.json()


@pytest_bdd.then('I have film comments')
def user_got_comments(context):
    assert context['resp'] == []


@pytest_bdd.when('I make create comment request with <given_text>')
def make_comment(given_text, user, context, client):
    genred_films = context['genred_films']
    session = user['session']

    resp = client.post("/api/v1/films/" + str(genred_films[0]['id']) + '/comments/',
                       {
                           'text': given_text
                       },
                       HTTP_AUTHORIZATION='Bearer ' + session)
    context['resp'] = resp.json()


@pytest_bdd.then('I have new comment')
def user_got_new_comment(context, given_text):
    assert context['resp']['text'] == given_text


@pytest_bdd.when('I make create Like request with <given_value>')
def create_like(given_value, user, context, client):
    genred_films = context['genred_films']
    session = user['session']

    resp = client.post("/api/v1/films/" + str(genred_films[0]['id']) + '/likes/',
                       {
                           'value': given_value
                       },
                       HTTP_AUTHORIZATION='Bearer ' + session)
    context['resp'] = resp.json()


@pytest_bdd.then('I have new like')
def user_got_like(context, given_value):
    assert context['resp']['value'] == given_value
