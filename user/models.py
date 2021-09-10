from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title= models.CharField(max_length=100)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    published_on= models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media")
    description= models.TextField()
    updated_on= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-published_on']

    def __str__(self) :
        return self.title
