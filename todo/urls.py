
from django.urls import path

from . import views


app_name = 'todo'


urlpatterns = [
    path('',
        views.IndexView.as_view(),
        name='index'),
    path(
        'api/index/',
        views.IndexAPIView.as_view()),
    path(
        'api/RecvTodos/',
        views.RecvDataView),
]