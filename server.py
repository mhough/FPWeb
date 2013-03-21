from index import base


def lo(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return base('Hello world!')
