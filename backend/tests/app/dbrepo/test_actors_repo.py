from modules.DBRepo.ActorDBRepo import ActorDBRepo


class TestActorsRepo:
    def test_get_success(self, simple_actor):
        # arrange
        expected_actor = ActorDBRepo.decode_orm_actor(simple_actor)
        test_id = simple_actor.id

        # act
        result_actor = ActorDBRepo.get(actor_id=test_id)

        # assert
        assert result_actor.first_name == expected_actor.first_name
        assert result_actor.last_name == expected_actor.last_name

    def test_get_fail_noe_found(self):
        # arrange
        test_id = 1

        # act
        result_actor = ActorDBRepo.get(actor_id=test_id)

        # assert
        assert result_actor is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = -100

        # act
        result_actor = ActorDBRepo.get(actor_id=test_id)

        # assert
        assert result_actor is None

    def test_get_all_success(self, actors_20):
        # arrange
        expected_actors = []
        for g in actors_20:
            expected_actors.append(ActorDBRepo.decode_orm_actor(g))

        # act
        result_actors = ActorDBRepo.get_all()

        # assert
        for i in range(len(expected_actors)):
            assert result_actors[i].first_name == expected_actors[i].first_name
            assert result_actors[i].last_name == expected_actors[i].last_name

    def test_get_all_no_results(self):
        # arrange
        expected_actors = []

        # act
        result_actors = ActorDBRepo.get_all()

        # assert
        assert result_actors == expected_actors
