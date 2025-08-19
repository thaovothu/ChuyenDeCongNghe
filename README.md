# Movie App

A simple Django project to manage movies and actors with relational queries, forms, and sample data.


## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/thaovothu/ChuyenDeCongNghe.git
   cd model


2. Create virtual environment and install dependencies
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt


3. Run migrations
    python manage.py makemigrations myapp
    python manage.py migrate


4. Create sample data
    python manage.py create_sample_movies


5. Run the server
    python manage.py runserver



## Features

- Models: Actor, Movie with Many-to-Many relationship
- Views: movie_list, add_movie
- Forms: MovieForm
- Templates: movie_list.html, movie_form.html
- Queries: relational and complex queries in Django shell
- Sample data: created via custom management command



## Usage

1. Visit movie list: http://127.0.0.1:8000/myapp/movies/
2. Add a new movie: http://127.0.0.1:8000/myapp/movies/add/
3. Test relational queries in Django shell:
   ```python
   from myapp.models import Actor, Movie
   leo = Actor.objects.get(name="Leonardo DiCaprio")
   leo.movies.all()
