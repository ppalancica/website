from django.urls import path
from . import views

urlpatterns = [
    # /courses/
    path('', views.index, name='index'),

    # /courses/35
    # url(r'^(?P<course_id>[0-9]+)/$')
    path('<int:course_id>/', views.detail, name='detail')
]
