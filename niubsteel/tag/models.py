from django.db import models
from users.models import User
from comment.models import Comment

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name

    @property
    def products(self):
        return [product_tag.from_comment.product for product_tag in ProductTag.objects.filter(tag=self)]

    @property
    def preview_products(self):
        return self.products[:5]

    @property
    def url(self):
        from django.core.urlresolvers import reverse
        return reverse('tag.views.tag_detail', kwargs={
            'tag_name': self.name,
        })

    @property
    def followers(self):
        from follow.models import TagFollow
        return [follow.user for follow in TagFollow.objects.filter(following=self)]

    def is_user_following(self, user):
        from follow.models import TagFollow
        return TagFollow.objects.filter(user=user, following=self).exists()

class ProductTag(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag)
    from_comment = models.ForeignKey(Comment)

    def __unicode__(self):
        return '#%s in "%s"' %(self.tag.name, self.from_comment.text[:20])

class ProductMention(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    mention = models.ForeignKey(User)
    from_comment = models.ForeignKey(Comment)

    def __unicode__(self):
        return '@%s in "%s"' %(self.mention.username, self.from_comment.text[:20])

from django.dispatch import receiver
from django.db.models.signals import post_save
import re

@receiver(post_save, sender=Comment)
def parse_comment(sender, **kwargs):
    comment = kwargs['instance']
    saved = kwargs['created']
    if not saved:
        return

    mentions = set(re.findall(ur'@(\S+)(?:\s|$)', comment.text))
    for mention in mentions:
        try:
            user = User.objects.get(username=mention)
            print ProductMention.objects.create(from_comment=comment, mention=user)
        except User.DoesNotExist:
            pass

    tag_names = set(re.findall(ur'#(\S+)(?:\s|$)', comment.text))
    for tag_name in tag_names:
        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(name=tag_name)
        print ProductTag.objects.create(from_comment=comment, tag=tag)
