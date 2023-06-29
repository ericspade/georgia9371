from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    category = models.CharField(max_length=64, unique=True)


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
