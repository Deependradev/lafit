from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=24)

    def delete_book(self):
        return "book has been deleted"
    
    def acquire_book(self):
        return "book has been acquired"