from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []


for i in range(1, 20):
    if i <= 5:
        genre = "detective"
    elif 5 < i <= 10:
        genre = "comedy"
    elif 10 < i <= 15:
        genre = "disaster"
    else:
        genre = "melodrama"
    movies.append(Movie(id=i, title=f"Title{i}", description=f"descr{i}", genre=genre))


@app.get("/", response_class=HTMLResponse)   # возвращаем HTML документ
async def get_all_movies(request: Request):
    return templates.TemplateResponse('list_movies.html', {'request': request, 'movies': movies})


@app.get("/movies/detective", response_class=HTMLResponse)
async def get_detective_movies(request: Request):
    movies_detective = []
    for movie in movies:
        if movie.genre == "detective":
            movies_detective.append(movie)
    return templates.TemplateResponse('list_movies.html', {'request': request, 'movies': movies_detective})


@app.get("/movies/disaster", response_class=HTMLResponse)
async def get_disaster_movies(request: Request):
    movie_disaster = []
    for movie in movies:
        if movie.genre == "disaster":
            movie_disaster.append(movie)
    return templates.TemplateResponse('list_movies.html', {'request': request, 'movies': movie_disaster})


@app.get("/movies/melodrama", response_class=HTMLResponse)
async def get_melodrama_movies(request: Request):
    movies_melodrama = []
    for movie in movies:
        if movie.genre == "melodrama":
            movies_melodrama.append(movie)
    return templates.TemplateResponse('list_movies.html', {'request': request, 'movies': movies_melodrama})


@app.post("/movies/create", response_model=Movie)
async def add_movies(movie: Movie):
    movie.id = len(movies) + 1
    movies.append(movie)
    print("movie is added successfully")
    return movie


@app.put("/movies/update/{movie_id}", response_model=Movie)
async def update_movies(movie_id: int, movie: Movie):
    for item in range(len(movies)):
        if movies[item].id == movie_id:
            movie.id = movie_id
            movies[item] = movie
            print(f'id = {movie.id} обновлен')
            return movie
    raise HTTPException(status_code=404, detail="movie not found")


@app.delete("/movies/delete/{movie_id}")
async def delete_movies(movie_id: int):
    for item in range(len(movies)):
        if movies[item].id == movie_id:
            del movies[item]
            return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")