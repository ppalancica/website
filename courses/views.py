from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course

class IndexView(generic.ListView):
    template_name = 'courses/index.html'

    # the default is object_list, but we want to use all_courses inside the views.py file
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

class CourseCreate(CreateView):
    model = Course
    fields = ['author', 'course_title', 'technology', 'course_logo']
