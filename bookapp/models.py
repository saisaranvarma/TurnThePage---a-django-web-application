from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150, null=True)


    def __str__(self):
        return '{}'.format(self.name)

class Book(models.Model):
    title=models.CharField(max_length=250,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')
    quantity=models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



    def __str__(self):
        return '{}'.format(self.title)


class Admin(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name