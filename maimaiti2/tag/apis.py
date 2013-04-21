
from restful.decorators import api

@api
def recommended_tags():
    from models import Tag
    tags = Tag.objects.filter(recommended=True)
    return [tag.view() for tag in tags]