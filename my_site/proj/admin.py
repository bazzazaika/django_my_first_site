from django.contrib import admin
from .models import Author, Document

# Register your models here.

admin.site.register(Document)
admin.site.register(Author)
