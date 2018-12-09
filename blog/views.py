from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
#from django.view.generic.dates import DayArchi
from .models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 이 옵션을 쓰지 않고, 디폴트 경로인 blog/post_list.html 을 쓰도록 하겠습니다.
    context_object_name = 'posts'  # 이 옵션을 쓰지 않고, 디폴트이름은 latest 를 쓰도록 하겠습니다.
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'