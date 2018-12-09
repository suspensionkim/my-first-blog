from django.views.generic import ListView, DetailView  # 추가
#from django.shortcuts import get_object_or_404, render  # 추가
from .models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    mode = Bookmark