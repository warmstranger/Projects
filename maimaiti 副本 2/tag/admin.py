from django.contrib import admin
from models import Tag, PostTag, CommentTag

admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(CommentTag)
