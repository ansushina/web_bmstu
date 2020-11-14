from typing import List

from app.models.Comment import CommentORM
from app.models.Profile import ProfileORM
from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.entities.Comment import Comment


class CommentDBRepo:
    @staticmethod
    def decode_orm_comment(orm_comment):
        orm_author = orm_comment.author

        return Comment(id=orm_comment.id,
                       text=orm_comment.text,
                       author=UserDBRepo.decode_orm_user_profile(orm_author),
                       film=orm_comment.film.id,
                       created=orm_comment.created_at
                       )

    @staticmethod
    def get(comment_id) -> Comment:
        orm_comment = CommentORM.objects.get(pk=comment_id)
        return CommentDBRepo.decode_orm_comment(orm_comment)

    @staticmethod
    def get_all(film_id, offset=0, limit=10) -> List[Comment]:
        orm_comments = CommentORM.objects.filter(film__id=film_id)[offset: offset+limit]
        comments = []
        for orm_comment in orm_comments:
            comments.append(CommentDBRepo.decode_orm_comment(orm_comment))
        return comments

    @staticmethod
    def create_comment(film_id, author_id, comment: Comment) -> Comment:
        orm_author = ProfileORM.objects.get(user=author_id)
        orm_comment = CommentORM.objects.create(
            text=comment.text,
            author_id=orm_author.id,
            film_id=film_id)
        orm_comment.save()
        return CommentDBRepo.decode_orm_comment(orm_comment)

    @staticmethod
    def update_comment(comment: Comment) -> Comment:
        orm_comment = CommentORM.objects.get(pk=comment.id)
        setattr(orm_comment, 'text', comment.text)
        orm_comment.save(update_fields=['text'])
        return CommentDBRepo.decode_orm_comment(orm_comment)

    @staticmethod
    def delete_comment(comment: Comment):
        orm_comment = CommentORM.objects.get(pk=comment.id)
        orm_comment.delete()


