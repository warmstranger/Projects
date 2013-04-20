#coding=utf-8

from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = u'用户资料'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'用户')
    image = models.ImageField(verbose_name=u'头像', blank=True, null=True, upload_to='profile_images')
    connected_user = models.CharField(max_length=100, verbose_name=u'关联用户', default=u'')
    is_buyer = models.BooleanField(verbose_name=u'买手', default=False)
    description = models.CharField(max_length=1000, default=u'', verbose_name=u'用户描述')

    def __unicode__(self):
        return '%s => %s' % (self.user.username, self.connected_user)

    def view(self):
        from follow.models import UserFollow
        follow_count = UserFollow.objects.filter(following=self.user).count()

        from post.models import Post
        posts = Post.objects.filter(author=self.user).order_by('-time')[:5]

        return {
            'username': self.user.username,
            'image_url': self.image.url if self.image else '',
            'is_buyer': self.is_buyer,
            'description': self.description,
            'follow_count': follow_count,
            'post_covers': [post.cover_image.url for post in posts],
        }

