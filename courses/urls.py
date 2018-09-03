from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'courses'

urlpatterns = [
    # /courses/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),


    # /courses/35
    # url(r'^(?P<course_id>[0-9]+)/$')
    # path('<int:course_id>/', views.detail, name='detail'),
    # path('<int:course_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /courses/35/favorite/
    # url(r'^(?P<course_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
    # path('<int:course_id>/favorite/', views.favorite, name='favorite')

    # /courses/course/add/
    url(r'course/add/$', views.CourseCreate.as_view(), name='course-add'),

    # /courses/course/2/
    url(r'course/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='course-update'),

    # /courses/course/2/delete/
    url(r'course/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete')

]
