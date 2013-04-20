#coding=utf-8

from restful import register_api, register_processor
from restful import Processor, get_processor
from exceptions import APIError

def api(func=None, name=None, **kwargs):
    processors = []
    for k, v in kwargs.iteritems():
        processor = get_processor(k, v)
        if processor:
            processors.append(processor)

    def decorator(api_func):
        api_name = api_func.__name__ if not name else name
        api_info = {
            'module': api_func.__module__,
            'function': api_func,
            'params': api_func.func_code.co_varnames[:api_func.func_code.co_argcount],
            'doc': api_func.__doc__,
            'processors': processors,
        }
        register_api(api_name, api_info)
        return api_func

    if func:
        return decorator(func)

    return decorator

def processor(Cls):
    register_processor(Cls)
    return Cls

@processor
class ContextProcessor(Processor):
    name = 'context'

    def process(self, request, params, api_info):
        context = {}
        if self.value:
            if 'request' in api_info['params']:
                context['request'] = request
            if 'user' in api_info['params']:
                context['user'] = request.user
        return context

@processor
class AuthProcessor(Processor):
    name = 'auth'

    def process(self, request, params, api_info):
        if self.value and not request.user.is_authenticated():
            raise APIError(403, u'需要登陆')

    def labels(self):
        if self.value:
            return [u'需要登陆']

@processor
class ConvertProcessor(Processor):
    name = 'convert'

    def process(self, request, params, api_info):
        context = {}
        if self.value:
            for k, v in self.value.iteritems():
                context[k] = v(params[k])
        return context

    def labels(self):
        if self.value:
            labels = []
            for k, v in self.value.iteritems():
                labels.append(u'%s: %s' % (k, v))
            return labels

@processor
class MethodProcessor(Processor):
    name = 'methods'

    def process(self, request, params, api_info):
        if self.value and request.method not in self.value:
            raise APIError(403, u'方法不允许')

    def labels(self):
        if self.value:
            labels = []
            for method in self.value:
                labels.append(u'需要%s' % method)
            return labels
