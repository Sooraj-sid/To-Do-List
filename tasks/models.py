from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    add_notes = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title