from django.db import models


class Note(models.Model):
    """
    Represents a simple text note.

    Fields:
    - title: Short title of the note.
    - content: Body/content of the note.
    - created_at: Timestamp when the note was created.
    - updated_at: Timestamp when the note was last updated.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # set once on create
    updated_at = models.DateTimeField(auto_now=True)      # updated on every save

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
