from modules.DBRepo.UserDBRepo import UserDBRepo


class TestUserRepo:
    def test_get_success(self, simple_profile):
        # arrange
        expected_profile = UserDBRepo.decode_orm_user_profile(simple_profile)
        test_username = expected_profile.username

        # act
        (result_profile, error) = UserDBRepo.get(test_username)

        # assert
        assert result_profile.id == expected_profile.id

    def test_get_fail_not_found(self):
        # arrange
        test_username = "blablablabla"

        # act
        (result_profile, error) = UserDBRepo.get(test_username)

        # assert
        assert error == "NotExist"

    def test_get_fail_not_normal(self):
        # arrange
        test_username = 1000

        # act
        (result_profile, error) = UserDBRepo.get(test_username)

        # assert
        assert error == "NotExist"

    def test_session_success(self, simple_profile, simple_profile_user):
        # arrange
        expected_profile = UserDBRepo.decode_orm_user_profile(simple_profile)
        test_user = simple_profile_user

        # act
        (result_session, error) = UserDBRepo.create_session(test_user)

        # assert
        assert error is None
        assert result_session.id == expected_profile.id

    def test_session_fail(self, simple_profile_user):
        # arrange
        test_user = simple_profile_user

        # act
        (result_session, error) = UserDBRepo.create_session(test_user)

        # assert
        assert error == "notExist"
