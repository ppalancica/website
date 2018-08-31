# from django.http import Http404
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.template import loader
from .models import Course

# Create your views here.

def index(request):
    all_courses = Course.objects.all()
    # template = loader.get_template('courses/index.html')
    context = { 'all_courses' : all_courses }

    return render(request, 'courses/index.html', context)

    # html = ''
    #
    # for course in all_courses:
    #     url = '/courses/' + str(course.id) + '/'
    #     html += '<a href="' + url + '">' + course.course_title + '</a><br/>'

    # return HttpResponse(template.render(context, request))

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # try:
    #     course = Course.objects.get(pk=course_id)
    # except Course.DoesNotExist:
    #     raise Http404("Album does not exist")

    return render(request, 'courses/detail.html', { 'course' : course })

    # return HttpResponse("<h2>Details for Course id: " + str(course_id) + "</h2>")
