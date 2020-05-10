from django.db import models


class Note(models.Model):
    """General ToDo Note Model."""

    summary = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.summary


class Task(models.Model):
    """Task model for all tasks on individual notes."""

    description = models.CharField(max_length=200)
    note = models.ForeignKey(
        Note, related_name="tasks", on_delete=models.CASCADE
    )
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.description
