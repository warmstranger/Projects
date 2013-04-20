#coding=utf-8

from restful.decorators import api

@api(convert={'start': int, 'count': int})
def recommended_posts(start, count):
    """
    推荐的帖子
    """
    from models import Post
    posts = Post.objects.order_by('-time')[start:start+count]
    return [post.view() for post in posts]

@api(convert={'start': int, 'count': int})
def posts_of_buyer(name, start, count):
    """
    买手的帖子
    """
    from models import Post
    posts = Post.objects.filter(author__username=name).order_by('-time')[start:start+count]
    return [post.view() for post in posts]

@api(convert={'start': int, 'count': int})
def posts_of_tag(name, start, count):
    """
    标签的帖子
    """
    from tag.models import PostTag
    post_tags = PostTag.objects.filter(tag__name=name)[start:start+count]
    return [post_tag.post.view() for post_tag in post_tags]