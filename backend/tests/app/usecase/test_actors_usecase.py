from pytest_mock import mocker

from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.entities.Actor import Actor
from modules.usecases.ActorUsecases import ActorUsecases
from tests.domain.ActorBuilder import ActorMother


class TestActorsUsecase:
    def test_get_success(self, mocker):
        # arrange
        expected_actors = [ActorMother.one().build(), ActorMother.two().build()]
        mocker.patch('modules.DBRepo.ActorDBRepo.ActorDBRepo.get_all', return_value=expected_actors)
        usecase = ActorUsecases(ActorDBRepo())

        # act
        result_actors = usecase.get_all_actors()

        # assert
        for i in range(len(expected_actors)):
            assert result_actors[i].first_name == expected_actors[i].first_name
            assert result_actors[i].last_name == expected_actors[i].last_name

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

    def test_get_one_success_london(self, mocker):
        # arrange
        usecase = ActorUsecases(ActorDBRepo())
        expected_actor = ActorMother.one().build()
        mocker.patch('modules.DBRepo.ActorDBRepo.ActorDBRepo.get', return_value=expected_actor)
        test_id = 1

        # act
        result_actors = usecase.get_actor(test_id)

        # assert
        assert result_actors.first_name == expected_actor.first_name
        assert result_actors.last_name == expected_actor.last_name

    # def test_get_one_no_result(self):
    #     usecase = ActorUsecases(ActorDBRepo())
    #
    #     result_actors = usecase.get_actor(1)
    #     assert result_actors is None
    #
    # def test_get_one_wrong_params(self):
    #     usecase = ActorUsecases(ActorDBRepo())
    #
    #     result_actors = usecase.get_actor(-100)
    #     assert result_actors is None
