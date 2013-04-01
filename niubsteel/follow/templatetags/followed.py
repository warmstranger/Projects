#coding=utf-8

from django import template
register = template.Library()

@register.filter
def followed(value, arg):
    if not arg.is_active:
        return False
    return value.is_user_following(arg)

@register.filter
def price(value):
    if value <= 0 or value > 100000:
        return u'电议'
    else:
        return value
