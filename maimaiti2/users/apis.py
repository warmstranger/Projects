
from restful.decorators import api

@api(context=True)
def get_user(request):
    return {
        'username': request.user.username
    } if request.user.is_authenticated() else None

@api
def recommended_buyers():
    from models import Profile
    buyers = Profile.objects.filter(is_buyer=True)[:4]
    return [buyer.view() for buyer in buyers]
