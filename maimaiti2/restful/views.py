#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from restful.apis import help
from restful import get_api
from exceptions import APIError
import json

def api_help(request):
    return render_to_response('help.html', {}, RequestContext(request))

@csrf_exempt
def api(request, api_name):
    kwargs = request.GET if request.method == 'GET' else request.POST
    params = {}
    for k, v in kwargs.iteritems():
        params[k] = v

    api_info = get_api(api_name)

    try:
        for processor in api_info['processors']:
            context = processor.process(request, params, api_info)
            if context:
                params.update(context)

        result = api_info['function'](**params)
        return HttpResponse(json.dumps(result))

    except APIError as ex:
        return HttpResponse(ex.data, status=ex.status)

    except Exception as ex:
        return HttpResponse(ex, status=500)
