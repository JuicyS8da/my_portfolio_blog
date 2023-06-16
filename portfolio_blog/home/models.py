from django.db import models
from django.urls import reverse
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug (auto)')
    short_desc = CKEditor5Field(config_name='extends', verbose_name='Short Description')
    content = CKEditor5Field(config_name='extends')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField('PostTags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-time_create', 'title']

    #delete cache when new post is created
    def save(self, *args, **kwargs):
        key = make_template_fragment_key('blog')
        cache.delete(key)

        return super().save(*args, **kwargs)

class Work(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug (auto)')
    short_desc = CKEditor5Field(config_name='extends', verbose_name='Short Description')
    content = CKEditor5Field(config_name='extends')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    github_link = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField('WorkTags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work', kwargs={'work_slug': self.slug})

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
        ordering = ['-time_create', 'title']

    # delete cache when new work is created
    def save(self, *args, **kwargs):
        key = make_template_fragment_key('works')
        cache.delete(key)

        return super().save(*args, **kwargs)


class PostTags(models.Model):
    name = models.CharField(max_length=12, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug (auto)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Post Tag'
        verbose_name_plural = 'Post Tags'

class WorkTags(models.Model):
    name = models.CharField(max_length=12, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug (auto)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('work_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Work Tag'
        verbose_name_plural = 'Work Tags'

class Resume(models.Model):
    file = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.file.name
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

class About(models.Model):
    greet = models.TextField(verbose_name='greet (HTML compatible):')
    desc = models.TextField(verbose_name='desc (HTML compatible):')
    photo = models.ImageField(upload_to='about/', verbose_name='photo (better pick square-sized like 768x768):')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'