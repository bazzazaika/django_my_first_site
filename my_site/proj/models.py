from django.db import models
import uuid
from django.urls import reverse


# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=1500, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    IMAGE_SELECT = (
        ('p', 'python'),
        ('C', 'C'),
    )
    image = models.CharField(max_length=1, choices=IMAGE_SELECT,blank=True,)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL,blank=True,)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/project/%i/" % self.id

class Author(models.Model):
    name = models.CharField(max_length=30, blank=True)
