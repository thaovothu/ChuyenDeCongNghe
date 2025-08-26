from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic import ListView
import asyncio

# --- Function-based views ---
def special_movie_1995(request):
    return HttpResponse("Phim nổi bật năm 1995: Toy Story ")

def movies_by_year(request, year):
    return HttpResponse(f"Các phim phát hành năm {year}")

def actor_detail(request, name):
    return HttpResponse(f"Thông tin diễn viên: {name}")

def show_current_time(request):
    return HttpResponse(f"Giờ hiện tại: {timezone.now()}")

def not_found_view(request):
    return HttpResponseNotFound(" Không tìm thấy nội dung!")

def forbidden_view(request):
    return HttpResponseForbidden(" Bạn không có quyền truy cập!")

def created_view(request):
    return HttpResponse(" Dữ liệu đã được tạo!", status=201)

async def async_show_time(request):
    await asyncio.sleep(1)
    return HttpResponse(f"(async) Bây giờ là: {timezone.now()}")



# --- Class-based views ---
class AboutView(View):
    def get(self, request):
        return HttpResponse("Đây là trang About - Ứng dụng Quản lý Phim & Diễn Viên")

class MovieListView(ListView):
    template_name = "myapp/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        return [
            {"title": "Inception", "year": 2010},
            {"title": "The Matrix", "year": 1999},
            {"title": "Interstellar", "year": 2014},
        ]

class AsyncView(View):
    async def get(self, request):
        await asyncio.sleep(1)
        return HttpResponse("Trả lời từ Async Class-based View")

# --- Template views ---
def template_demo(request):
    data = {"movies": ["Avatar", "Titanic", "Joker"]}
    return render(request, "myapp/template_demo.html", data)

def external_template(request):
    data = {"actor": "Leonardo DiCaprio", "movies": ["Inception", "The Revenant"]}
    return render(request, "outside_template.html", data)


def movie_list(request):
    movies = [
        {"title": "Inception", "year": 2010},
        {"title": "Interstellar", "year": 2014},
        {"title": "Oppenheimer", "year": 2023},
    ]
    return render(request, "myapp/movie_list.html", {"movies": movies})