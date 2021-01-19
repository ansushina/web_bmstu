from django.http import HttpRequest

from app.views.CommentView import CommentView
from app.views.CommentsListView import CommentsListView
from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.entities.Comment import Comment
from tests.domain.CommentBuilder import CommentMother


def commentToDict(comment: Comment):
    return {
        'text': comment.text,
        'id': comment.id
    }


class TestCommentView:
    def test_get_mock(self, client, mocker):
        # arrange
        test_comment = CommentMother.one().build()
        test_id = 1
        mocker.patch('modules.DBRepo.CommentDBRepo.CommentDBRepo.get', return_value=test_comment)
        view = CommentView()

        # act
        resp = view.get(HttpRequest(), 1,  test_id)

        # assert
        assert commentToDict(test_comment)['text'] == resp.data['text']


    def test_all_mock(self, client, mocker):
        # arrange
        test_comments = [CommentMother.one().build(), CommentMother.two().build()]
        mocker.patch('modules.DBRepo.CommentDBRepo.CommentDBRepo.get_all', return_value=test_comments)
        expected_resp = [commentToDict(test_comments[i]) for i in range(len(test_comments))]
        view = CommentsListView()

        # act
        resp = view.get(HttpRequest(), test_comments[0].film)

        # assert
        for i in range(len(expected_resp)):
            assert expected_resp[i]['text'] == resp.data[i]['text']

    # def test_get_comment(self, simple_comment, client):
    #     # arrange
    #     test_comment = CommentDBRepo.decode_orm_comment(simple_comment)
    #
    #     # act
    #     resp = client.get("/api/v1/films/" + str(test_comment.film) + "/comments/" + str(test_comment.id) + "/")
    #
    #     # assert
    #     assert commentToDict(test_comment)['text'] == resp.json()['text']
    #
    # def test_get_all_comments(self, comments_20, client):
    #     # arrange
    #     test_comments = [CommentDBRepo.decode_orm_comment(comments_20[i]) for i in range(len(comments_20))]
    #     expected_resp = [commentToDict(test_comments[i]) for i in range(len(test_comments))]
    #     expected_len = 10
    #
    #     # act
    #     resp = client.get("/api/v1/films/" + str(test_comments[0].film) + "/comments/")
    #
    #     # assert
    #     for i in range(expected_len):
    #         assert expected_resp[i]['text'] == resp.json()[i]['text']
