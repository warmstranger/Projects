
from restful.decorators import api

@api(context=True, auth=True, convert={'product': int})
def save(product):
    pass