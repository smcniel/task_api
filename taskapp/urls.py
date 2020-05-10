"""Django taskapp urls."""

from django.urls import path
from .views import NoteList, NoteDetail, TaskList, TaskDetail

urlpatterns = [
    path("notes/", NoteList.as_view(), name="notes_list"),
    path("notes/<int:pk>/", NoteDetail.as_view(), name="notes_detail"),
    path("notes/<int:pk>/tasks/", TaskList.as_view(), name="tasks_list"),
    path(
        "notes/<int:pk>/tasks/<int:task_pk>/",
        TaskDetail.as_view(), name="tasks_detail"
    )
]
