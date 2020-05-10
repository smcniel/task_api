from .models import Note, Task


def seed_data(data):
    for note in data:
        new_note = Note.objects.create(summary=note)
        new_note.save()
        current_note = Note.objects.last()

        for task in data[note]:
            new_task = Task.object.create(
                note=current_note, description=task
            )
            new_task.save()


data = {
    "finish backyard": ["sweep leaves", "plant herbs", "clean grill"],
    "website design": [
        "wireframe", "confirm colors with client", "setup NGINX as proxy"
    ],
    "get supplies for party": [
        "buy food on list", "wine and liquor", "rent more seating"
    ]
}

seed_data(data)
