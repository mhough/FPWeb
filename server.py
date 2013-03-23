'''
Generic(-ish) view functions and WSGI apps and things to modify same.
'''
from functools import wraps
from templates import base


def lo(environ, start_response):
  '''
  Render a page in environ['PAGE'] using the base template.
  '''
  start_response('200 OK', [('content-type', 'text/html')])
  return base(**environ.get('PAGE', {}))


def css(environ, start_response):
  '''
  Render a page in environ['PAGE'] using the base template.
  '''
  start_response('200 OK', [('content-type', 'text/css')])
  return environ.get('CSS', 'NOT REALLY CSS YO!')


def envey(**kw):
  '''
  Modify environ.
  '''
  def decorator(view_function):
#    @wraps(view_function)
    def a(environ, start_response):
      environ.update(kw)
      return view_function(environ, start_response)
    return a
  return decorator


