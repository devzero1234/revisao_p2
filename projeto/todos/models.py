from django.db import models
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at =models.DateField(auto_now_add=True,null=False,blank=False)
    deadline = models.DateField(null=False, blank=False)
    deadline = models.DateField()
    finished_at = models.DateField(null=True)

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)  # ✔️
    due_date = models.DateField(null=True, blank=True)  # 📅
    priority = models.IntegerField(default=1)  # ⬆️ 1=baixa, 2=média, 3=alta

    def __str__(self):
        return self.title
    
completed = models.BooleanField(default=False)