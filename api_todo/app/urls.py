from app.views import TodoListAndCreate, TodoDetailChangeDelete
from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeDelete.as_view()),
]