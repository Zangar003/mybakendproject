from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.db import models

class Question(models.Model):
    questiopn_text =models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    class Meta:
        verbose_name ="Сқрақ"
        verbose_name_plural = "Сұрақтар"

class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ="Мақала"
        verbose_name_plural = "Мақалалар"



class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Zagalovok")
    is_published = models.BooleanField(default=True, verbose_name="publication")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name ="Мекен жаи"
        verbose_name_plural = "мекен жаилар"



# Create your models here.
class Form_lab(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.CharField(max_length=255, verbose_name="chekbox")
    is_published = models.BooleanField(default=True)
    picture = models.ImageField()
    email = models.EmailField(blank=True)
    questiopn_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    def get_number(self):
        return 10
    def get_boolean(self):
        if 7 +7 == 14:
            return True
    def get_length(self):
        for i in range(1, 10):
            if i == 8:
                return i
