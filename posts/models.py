from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    ''' Posts Details '''

    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='post_image')
    post_like_count = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class Like(models.Model):
    ''' like  posts '''

    post = models.OneToOneField(Post, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requirement_posts_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.post_title)[:30]

class DisLike(models.Model):
    ''' Dislike  posts '''

    post = models.OneToOneField(Post, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requirement_posts_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.post_title)[:30]
