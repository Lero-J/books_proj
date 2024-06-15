from django.db import models

# Create your models here.



from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/%d-%m-%y', null=True, blank=True)
    bio = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['id']



class Book(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to='books/%d-%m-%y', null=True, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    category = models.ManyToManyField(Category, related_name='books', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['id']







