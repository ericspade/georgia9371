from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import notify_subscribers_news_createdtask


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        author_posts = Author.objects.get(pk=1).post_set.all().values('rating')
        author_posts = list(author_posts)
        for i in author_posts:
            count = int(author_posts[i - 1]['rating'])
            totalposts = totalposts + count
            print(totalposts)


class Category(models.Model):
    category = models.TextField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=64, unique=True)
    article_text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = self.rating + 1
        self.save()

    def dislike(self):
        self.rating = self.rating - 1
        self.save()

    def preview(self):
        print(self.article_text[:124], '...')

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = self.rating + 1
        self.save()

    def dislike(self):
        self.rating = self.rating - 1
        self.save()


@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers_news_created(sender, instance, action, **kwargs):
    notify_subscribers_news_createdtask.delay(instance.pk, action)
