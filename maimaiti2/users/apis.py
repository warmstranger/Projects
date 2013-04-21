
from restful.decorators import api

@api(context=True)
def get_user(request):
    return {
        'username': request.user.username,
        'is_buyer': request.user.profile.is_buyer,
    } if request.user.is_authenticated() else None

@api(convert={'count': int})
def get_buyers(count=20):
    from models import Profile
    buyers = Profile.objects.filter(is_buyer=True)[:count]
    return [buyer.view() for buyer in buyers]

@api
def recommended_buyers():
    from models import Profile
    buyers = Profile.objects.filter(is_buyer=True, is_recommended=True)
    return [buyer.view() for buyer in buyers]

