def main():
    N = int(input().strip())

    movies = []

    for _ in range(N):
        year = int(input().strip())
        name = input().strip()
        category = input().strip()
        screening = input().strip()
        movies.append((year, name, category, screening))

    query = input().strip()

    if query.isdigit():
        query = int(query)
        queried_movies = [movie for movie in movies if movie[0] == query]
        if queried_movies:
            print(query)
            print()
            for movie in queried_movies:
                print(movie[1])
                print(movie[2])
                print(movie[3])
                print()
        else:
            print("Sem filmes nessa consulta")
    else:
        queried_movies = [movie for movie in movies if movie[2] == query]
        if queried_movies:
            print(query)
            print()
            for movie in queried_movies:
                print(movie[0])
                print(movie[1])
                print(movie[3])
                print()
        else:
            print("Sem filmes nessa consulta")

if __name__ == "__main__":
    main()