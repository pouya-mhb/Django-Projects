from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post (models.Model):
    STATUS_CHOICES = (
        # todo ('editing','Editing')
        ('draft' , 'Draft'),
        ('published' , 'Published')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_lenght=100 , unique_for_date='publish_date')
    published_at = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    upadted_date = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')

    class Meta :
        ordering = ('-publish', )

        def __str__(self) -> str:
            return self.title