from pytest_mock import mocker

from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.entities.Actor import Actor
from modules.usecases.ActorUsecases import ActorUsecases
from tests.domain.ActorBuilder import ActorMother


class TestActorsUsecase:
    def test_get_one_success(self, simple_actor):
        # arrange
        test_id = simple_actor.id
        usecase = ActorUsecases(ActorDBRepo())
        expected_actor = ActorDBRepo.decode_orm_actor(simple_actor)

        # act
        result_actors = usecase.get_actor(test_id)

        # assert
        assert result_actors.first_name == expected_actor.first_name
        assert result_actors.last_name == expected_actor.last_name

    def test_get_one_no_result(self):
        usecase = ActorUsecases(ActorDBRepo())

        result_actors = usecase.get_actor(1)
        assert result_actors is None

    def test_get_one_wrong_params(self):
        usecase = ActorUsecases(ActorDBRepo())

        result_actors = usecase.get_actor(-100)
        assert result_actors is None
