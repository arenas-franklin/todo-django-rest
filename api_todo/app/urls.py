from app.views import todo_list, todo_detail_change_and_delete
from django.urls import path

urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_detail_change_and_delete),
]