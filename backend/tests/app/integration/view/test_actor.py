from django.http import HttpRequest, HttpResponse
from rest_framework.request import Request

from app.views.ActorView import ActorView
from app.views.ActorsListView import ActorsListView
from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.entities.Actor import Actor
from tests.domain.ActorBuilder import ActorMother


def actorToDict(actor: Actor):
    return {
        'first_name': actor.first_name,
        'last_name': actor.last_name,
        'id': actor.id
    }


class TestActorView:
    def test_get_mock(self, client, mocker):
        # arrange
        test_actor = ActorMother.one().build()
        test_id = 1
        mocker.patch('modules.DBRepo.ActorDBRepo.ActorDBRepo.get', return_value=test_actor)
        view = ActorView()

        # act
        resp = view.get(HttpRequest(), test_id)

        # assert
        assert actorToDict(test_actor) == resp.data

    def test_all_mock(self, client, mocker):
        # arrange
        test_actors = [ActorMother.one().build(), ActorMother.two().build()]
        mocker.patch('modules.DBRepo.ActorDBRepo.ActorDBRepo.get_all', return_value=test_actors)
        expected_resp = [actorToDict(test_actors[i]) for i in range(len(test_actors))]
        view = ActorsListView()

        # act
        resp = view.get(HttpRequest())

        # assert
        assert expected_resp == resp.data

        # def test_get_actor(self, simple_actor, client):
        #     # arrange
        #     test_actor = ActorDBRepo.decode_orm_actor(simple_actor)
        #
        #     # act
        #     resp = client.get("/api/v1/actors/" + str(test_actor.id) + "/")
        #
        #     # assert
        #     assert actorToDict(test_actor) == resp.json()
        #
        # def test_get_all_actors(self, actors_20, client):
        #     # arrange
        #     test_actors = [ActorDBRepo.decode_orm_actor(actors_20[i]) for i in range(len(actors_20))]
        #     expected_resp = [actorToDict(test_actors[i]) for i in range(len(test_actors))]
        #
        #     # act
        #     resp = client.get("/api/v1/actors/")
        #
        #     # assert
        #     assert expected_resp == resp.json()
