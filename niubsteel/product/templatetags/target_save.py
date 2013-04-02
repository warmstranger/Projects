from django import template
register = template.Library()


@register.filter
def target_save_by_collection(product, collection):
    return product.target_save_by_collection(collection)


@register.filter
def target_save_by_user(product, user):
    return product.target_save_by_user(user)
