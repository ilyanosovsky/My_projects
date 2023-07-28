from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True, blank=True)
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f'{self.category} | {self.title}' 