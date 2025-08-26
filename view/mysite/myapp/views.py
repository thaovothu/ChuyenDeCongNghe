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
