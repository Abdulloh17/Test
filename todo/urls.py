from django.urls import path

from todo.views import TodoCreateApi, ToDoDetailApi

urlpatterns = [
    path('api/todos/', TodoCreateApi.as_view(), name='todos'),
    path('api/todos/<int:pk>', ToDoDetailApi.as_view(), name='crud-todo'),
]
