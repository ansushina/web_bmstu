from modules.entities.Comment import Comment


class CommentMother:
    @staticmethod
    def one():
        comment = CommentBuilder()
        comment.text = 'comment1'
        return comment

    @staticmethod
    def two():
        comment = CommentBuilder()
        comment.text = 'comment2'
        return comment


class CommentBuilder:
    def __init__(self):
        self.text = ""
        self.author = 1
        self.film = 1
        self.created = None
        self.id = None

    def build(self):
        return Comment(text=self.text,
                       author=self.author,
                       film=self.film,
                       created=self.created,
                       id=self.id)
