
from restful.decorators import api

@api(auth=True, context=True, convert={'follow_id': int})
def toggle_follow(follow_type, follow_id, request):
    pass