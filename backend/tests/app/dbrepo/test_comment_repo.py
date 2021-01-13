from modules.DBRepo.CommentDBRepo import CommentDBRepo


class TestCommentsRepo:
    def test_get_success(self, simple_comment):
        # arrange
        expected_comment = CommentDBRepo.decode_orm_comment(simple_comment)
        test_id = simple_comment.id

        # act
        result_comment = CommentDBRepo.get(comment_id=test_id)

        # assert
        assert result_comment.text == expected_comment.text

    def test_get_fail_not_found(self):
        # arrange
        test_id = 1

        # act
        result_comment = CommentDBRepo.get(comment_id=test_id)

        # assert
        assert result_comment is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = -100

        # act
        result_comment = CommentDBRepo.get(comment_id=-test_id)

        # assert
        assert result_comment is None

    def test_get_all_success(self, comments_20):
        # arrange
        expected_comments = []
        for g in comments_20:
            expected_comments.append(CommentDBRepo.decode_orm_comment(g))

        # act
        result_comments = CommentDBRepo.get_all(expected_comments[0].film)

        # assert
        for i in range(10):
            assert result_comments[i].text == expected_comments[i].text

    def test_get_all_no_results(self):
        # arrange
        expected_comments = []

        # act
        result_comments = CommentDBRepo.get_all(1)

        # accert
        assert result_comments == expected_comments
