from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo, name='todo'),  # View all todos
    path('todoadd/', views.add, name='todoadd'),  # Add a new todo
    path('delete/<int:id>/', views.delete, name='delete'),  # Delete a specific todo
    path('delete/', views.delete_all, name='delete_all'),  # Delete all todos
]
