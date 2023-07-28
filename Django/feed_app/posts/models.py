from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# POST 

CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('Js', 'JavaScript'),
    ('Py', 'Python')
) 
# value on the left is what is stored in the database
# value on the right is what is displayed in the admin panel



class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    publlish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title