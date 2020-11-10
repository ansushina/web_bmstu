class Film:
    def __init__(self,
                 title,
                 description,
                 year,
                 genres,
                 actors,
                 countries,
                 image,
                 created,
                 comments,
                 rating=0,
                 id=None):
        self.id = id
        self.title = title
        self.description = description
        self.year = year
        self.rating = rating
        self.genres = genres
        self.actors = actors
        self.countries = countries
        self.image = image
        self.created = created
        self.comments = comments

        @property
        def title(self):
            return self.title


