from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

class Book(models.Model):
    def __str__(self):
        return self.book_title
    book_title=models.CharField(max_length=200)
    book_author=models.CharField(max_length=200)
    book_description=models.TextField()
    available=models.BooleanField(default=True)