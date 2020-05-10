# Setup Notes:

An example .env file is given to be used with python-decouple.

Seed data for the database with seed_data.py (needs to be refactored for django)

# Project Notes:

### Notes vs Tasks

A "Note" is defined as a general TO DO item, while a "Task" is one of many individual steps needed to finalize a Note.

You can list all notes, add or delete a note.  You cannot update the note's fields.  You can only update the tasks associated with the note. 

Currently, the list overview excludes the tasks associated with each note, with the thought that someone would design a dashboard of just note listings without the overhaul of fetching all the tasks associated with it from the database.

The views for a Note model are separated due to the different querysets and serializers. I found this to be cleaner than writing the custom router logic.


### Further Optimization

Ways to optimize in future versions

  - Possibly restricting task fields that can be updated
  - Automatically deleting note when all tasks are completed
  - Adding user validation and/or login
  - Obviously a better database engine (Postsql instead of sqlite)
  - SSL, NGINX server proxy, and other server security measures
  - Refactoring of cleaner viewsets and adding REST framework routers
  - Possibly serialize Tasks as hyperlinks



