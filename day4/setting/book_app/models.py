from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_description = models.TextField()
    book_type = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    price = models.IntegerField()
    book_quantity = models.IntegerField()

    def __str__(self):
        return self.book_title