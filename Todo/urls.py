from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:task_id>', views.delete, name="delete"),
    path('update/<int:task_id>', views.update, name="update"),
    path('complete_task/<int:task_id>', views.complete_task, name="complete_task")
]