from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

# DJANGO - ORM => Object Relational Mapping
# models.py ma main class jati tali update garyo teti tali (py manage.py makemigration) garna parxa ani physical database ma jana (py manage.py migration) garni
class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class News(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField("Category",related_name="news_categories")# string ma ralhya vani yo class tala ni kam garxa mathi pani
    count = models.IntegerField(default=0)# trending news ko lgi views count garna
    slug = models.SlugField(max_length=255,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)# on delete means edi tyo author le xodera gaye pani news delete nahuni...news company ko property ho
    created_at = models.DateTimeField(auto_now_add=True)# add garesi updae hunna,add garya time matra basxa
    updated_at = models.DateTimeField(auto_now=True)# update hunxa, update garya matra time basxa
    cover_image = models.ImageField(upload_to="news", null=True)
    
    
    def get_absolute_url(self): # absolute_url gives direct jumb to object view
        return reverse("single_news", kwargs={"pk": self.pk, "slug": self.slug})


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)