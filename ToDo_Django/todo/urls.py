from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTaskView.as_view(), name="list-task-view"),
    path("delete/<int:pk>", views.DeleteTaskView.as_view(), name="delete-task-view"),
    path(
        "complete/<int:pk>", views.CompleteTaskView.as_view(), name="complete-task-view"
    ),
    path(
        "not-complete/<int:pk>",
        views.NotCompleteTaskView.as_view(),
        name="not-complete-task-view",
    ),
    path("create", views.CreateTaskView.as_view(), name="create-task-view"),
    path("update/<int:pk>", views.UpdateTaskView.as_view(), name="update-task-view"),
]
