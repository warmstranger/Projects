
from restful.decorators import api

@api(context=True, auth=True)
def comment(text, request=None):
    """
    Text
    """

@api(context=True, auth=True)
def delete_comment(id, request=None):
    """
    Delete comment
    """