from django.db import models
from accounts.models import User


class Todo(models.Model):
    TYPE_CHOICES = (
        ('1', 'Todo'),
        ('2', 'Doing'),
        ('3', 'Done'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    contents = models.TextField()
    contents_type = models.CharField(choices=TYPE_CHOICES, max_length=16, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)

    class Meta:
        ordering = ['-create_date']