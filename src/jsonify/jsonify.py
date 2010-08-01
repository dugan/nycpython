from django.utils import simplejson

from django.http import HttpResponse, HttpResponseServerError


class JSONResponse(object):
    def __init__(self, data=None, response_class=HttpResponse):
        self.data = data
        self.response_class = response_class

    def __freeze__(self):
        return self.data

    def get_response(self):
        return self.response_class(simplejson.dumps(self.__freeze__()),
                                   mimetype="application/json")

class JSONError(JSONResponse):
    def __init__(self, msg):
        JSONResponse.__init__(self, {'msg' : msg },
                              response_class=HttpResponseServerError)

class JSONFormError(JSONError):
    def __init__(self, form):
        JSONError.__init__(self, msg=', '.join(form.errors))

def error_response(**kwargs):
    return JSONResponse(kwargs,
                       response_class=HttpResponseServerError).get_response()

def response(**kwargs):
    return JSONResponse(kwargs).get_response()
