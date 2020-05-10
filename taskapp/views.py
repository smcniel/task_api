from rest_framework import generics
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status

from .models import Note, Task
from .serializers import NoteSerializer, NoteDetailSerializer, TaskSerializer


class NoteList(generics.ListCreateAPIView):
    """GET overview of all notes or POST new note.  Overviews exclude tasks."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveDestroyAPIView):
    """Retreive individual details, or delete.  Allows GET and DELETE."""

    queryset = (Note.objects.prefetch_related('tasks', ))
    serializer_class = NoteDetailSerializer


class TaskList(generics.ListCreateAPIView):
    """GET all tasks for specific note and POST new task."""

    serializer_class = TaskSerializer

    def get_queryset(self):
        """Override queryset to filter for passed in note id."""
        queryset = Task.objects.filter(note_id=self.kwargs["pk"])
        return queryset


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or destroy specific task."""

    def get_queryset(self):
        """Override queryset to filter for passed in note id."""
        queryset = Task.objects.filter(note_id=self.kwargs["pk"])
        return queryset

    serializer_class = TaskSerializer
