from django.db import models
from todoapp.models import Todo
from accounts.models import User

class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)