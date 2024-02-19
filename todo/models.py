from django.db import models

status_choices = (
    ("New", "New"),
    ("In Progress", "In Progress"),
    ("Done", "Done")
)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField("due_date")
    status = models.CharField(max_length=20, choices=status_choices, default="New")

    def __str__(self):
        return self.title
