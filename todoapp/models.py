from django.db import models
from accounts.models import User


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['-create_date']
    
    def __str__(self):
        return self.title
    

class Todo(models.Model):
    TYPE_CHOICES = (
        ('1', 'Todo'),
        ('2', 'Doing'),
        ('3', 'Done'),
    )

    projects = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    contents = models.TextField()
    contents_type = models.CharField(choices=TYPE_CHOICES, max_length=16, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    view = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        ordering = ['-create_date']