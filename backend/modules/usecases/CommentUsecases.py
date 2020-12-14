from typing import List

from modules.entities.Comment import Comment


class CommentUsecases:
    def __init__(self, comment_repo):
        self.comment_repo = comment_repo

    def get_comment(self, comment_id) -> Comment:
        comment = self.comment_repo.get(comment_id)
        return comment

    def get_all_comments(self, film_id, offset, limit) -> List[Comment]:
        comments = self.comment_repo.get_all(film_id, offset, limit)
        return comments

    def create_comment(self, film_id, user_id, text):
        comment = Comment(text=text)
        new_comment = self.comment_repo.create_comment(
            film_id=film_id,
            author_id=user_id,
            comment=comment)
        return new_comment

    def update_comment(self, comment_id, text):
        comment = Comment(text=text, id=comment_id)
        new_comment = self.comment_repo.update_comment(
            comment=comment
        )
        return new_comment

    def delete_comment(self, comment_id):
        comment = Comment(id=comment_id, text='')
        self.comment_repo.delete_comment(comment)
