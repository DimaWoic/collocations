from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='category', default='')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Collocation(models.Model):
    phrase = models.CharField(max_length=250, verbose_name='a phrase or a word', default='')
    translation = models.CharField(max_length=250, verbose_name='translation', default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    publish = models.BooleanField(verbose_name='publish', default=False)

    class Meta:
        verbose_name = 'collocation'
        verbose_name_plural = 'collocations'

    def __str__(self):
        return self.phrase
