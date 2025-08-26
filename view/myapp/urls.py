from django.urls import path
from . import views

urlpatterns = [
    path("movies/1995/", views.special_movie_1995),   
    path("movies/<int:year>/", views.movies_by_year), 
    path("actors/<str:name>/", views.actor_detail),   
    path("now/", views.show_current_time, name="now"),  
    path("notfound/", views.not_found_view, name="notfound"),
    path("forbidden/", views.forbidden_view, name="forbidden"),
    path("created/", views.created_view, name="created"),
    path("asyncnow/", views.async_show_time, name="asyncnow"),
    
    # Class-based views
    path("about/", views.AboutView.as_view(), name="about"),
    path("movies-list/", views.MovieListView.as_view(), name="movies_list"),
    path("asyncview/", views.AsyncView.as_view(), name="async_view"),

    # # Template views
    # path("template-demo/", views.template_demo, name="template_demo"),
    # path("external-template/", views.external_template, name="external_template"),

]
