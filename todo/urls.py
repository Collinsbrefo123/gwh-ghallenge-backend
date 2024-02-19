from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'todo'
router = DefaultRouter()
router.register('todo', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('get_all', views.TodoView().as_view(), name='get_todos'),
    path('send-todo', views.TodoView().as_view(), name='post_todos'),
    path("", include(router.urls))
]
