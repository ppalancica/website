# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Course

# Create your views here.

def index(request):
    all_courses = Course.objects.all()
    template = loader.get_template('courses/index.html')
    context = {
        'all_courses' : all_courses
    }

    # html = ''
    #
    # for course in all_courses:
    #     url = '/courses/' + str(course.id) + '/'
    #     html += '<a href="' + url + '">' + course.course_title + '</a><br/>'

    return HttpResponse(template.render(context, request))

def detail(request, course_id):
    return HttpResponse("<h2>Details for Course id: " + str(course_id) + "</h2>")
