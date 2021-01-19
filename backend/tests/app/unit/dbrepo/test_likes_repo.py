from modules.DBRepo.LikeDBRepo import LikeDBRepo


class TestLikesRepo:
    def test_get_success(self, simple_like):
        # arrange
        start_like = LikeDBRepo.decode_orm_like(simple_like)
        test_id = simple_like.id

        # act
        result_like = LikeDBRepo.get(like_id=test_id)

        # assert
        assert result_like.value == start_like.value

    def test_get_fail_not_found(self):
        # arrange
        test_id = 1

        # act
        result_like = LikeDBRepo.get(like_id=test_id)

        # assert
        assert result_like is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = -100

        # act
        result_like = LikeDBRepo.get(like_id=test_id)

        # assert
        assert result_like is None
