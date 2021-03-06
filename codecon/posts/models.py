from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

CATEGORIES = (
        ('Algorithm Analysis', 'Algorithm Analysis'),
        ('Language Theory', 'Language Theory'),
        ('Mobile Development', 'Mobile Development'),
        ('Web Development', 'Web Development'),
        ('Web Security', 'Web Security'),
        ('Data Structures', 'Data Structures'),
        ('General Programming', 'General Programming'),
    )

LANGUAGES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('C', 'C'),
        ('Assembly', 'Assembly'),
        ('Javascript', 'Javascript'),
    )

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    date_created = models.DateTimeField()
    owner = models.ForeignKey(User)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='General Programming')
    language = models.CharField(max_length=100, choices=LANGUAGES, default='C')
    slug = models.SlugField()

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    @property
    def get_score(self):
        num_likes = self.likes.all().count()
        num_comments = self.comments.all().count()
        return num_likes + num_comments

class Like(models.Model):
    liker = models.ForeignKey(User)
    like_date = models.DateTimeField(auto_now=True)
    liked_post = models.ForeignKey(Post, related_name="likes")

    def __unicode__(self):
        return self.liker.username


class FileUpload(models.Model):
    file_upload = models.FileField(upload_to='post_uploads/%Y/%m/%d/')
    file_post = models.ForeignKey(Post, related_name="documents")
    upload_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.file_post.title
