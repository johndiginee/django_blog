from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """Represent a blog post.
    
    Attributes:
        title (str): The post title
        slug (str): The post slug.
        author (int): The post author.
        body (str): The body of the post.
        publish (str): The post publish date and time
        created (str): The post created date and time
        updated (str): The post updated date and time
        status (str): The post publish status
    """
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title