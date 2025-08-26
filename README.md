# LAB2_Movie App

A simple Django project to manage movies and actors with relational queries, forms, and sample data.


## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/thaovothu/ChuyenDeCongNghe.git
   cd model


2. Create virtual environment and install dependencies
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt


3. Run migrations
    ```bash
    python manage.py makemigrations myapp
    python manage.py migrate


4. Create sample data
    ```bash
    python manage.py create_sample_movies


5. Run the server
    ```bash
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







# LAB3_Movie App

A simple Django project to manage movies and actors with relational queries, forms, and sample data.


## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/thaovothu/ChuyenDeCongNghe.git
   cd model


2. Create virtual environment and install dependencies
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt


3. Run migrations
    ```bash
    python manage.py makemigrations myapp
    python manage.py migrate


4. Run the server
    ```bash
    python manage.py runserver



## Features

- Models: Actor: name, birth_year. Movie: title, release_year, many-to-many with Actor
- Function-based Views: special_movie_1995: movie highlight in 1995. 
  movies_by_year: list movies by year
  actor_detail: show actor info
  show_current_time: display current time
  not_found_view: return 404
  forbidden_view: return 403
  created_view: return 201 status
- Class-based Views: AboutView: display about page. MovieListView: list of movies using template myapp/movies.html. MovieListView: list of movies using template myapp/movies.html
- Template Views: template_demo: render myapp/template_demo.html with sample movies. external_template: render outside_template.html with actor info



## URL Config
1. Function-based URLs:
    /movies/1995/ → special_movie_1995
    /movies/<int:year>/ → movies_by_year
    /actors/<str:name>/ → actor_detail
    /now/ → show_current_time
    /notfound/ → not_found_view
    /forbidden/ → forbidden_view
    /created/ → created_view
    /asyncnow/ → async_show_time

2. Class-based URLs
    /about/ → AboutView
    /movies-list/ → MovieListView
    /asyncview/ → AsyncView

3. Template URLs
   /template-demo/ → template_demo
   /external-template/ → external_template



## Usage

1. Visit movie list: http://127.0.0.1:8000/movies-list/
2. Visit about page: http://127.0.0.1:8000/about/
3. Test relational queries in Django shell:
   ```python
   from myapp.models import Actor, Movie
    leo = Actor.objects.get(name="Leonardo DiCaprio")
    leo.movies.all()

4. Test async view: http://127.0.0.1:8000/asyncnow/
5. Test templates:
    http://127.0.0.1:8000/template-demo/
    http://127.0.0.1:8000/external-template/

