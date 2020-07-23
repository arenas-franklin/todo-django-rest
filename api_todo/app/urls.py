from app.views import todo_list
from django.urls import path

urlpatterns = [
    path('', todo_list),
]