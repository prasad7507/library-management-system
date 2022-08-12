from django.db import models,connections

# Create your models here.


class Users(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True,unique=True)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='users'
class BooksDetails(models.Model):
    book_id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=100)
    book_description=models.CharField(max_length=500)
    class Meta:
        db_table='books'
