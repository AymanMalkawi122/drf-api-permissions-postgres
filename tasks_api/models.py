from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('task_list')