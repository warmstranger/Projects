
from restful.decorators import api

@api
def help():
    print 11
    import restful
    return restful.docs.items()

