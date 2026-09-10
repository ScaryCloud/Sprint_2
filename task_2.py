class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movie = movie
        self.movies.append(self.movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драммы: '{self.movies}'"

comedy = Comedy()
drama = Drama()

comedy_result = comedy.add_movie('Большой куш')
print(comedy_result)
drama_result = drama.add_movie('Оружейный барон')
print(drama_result)
