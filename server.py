from wsgiref.simple_server import make_server
import selector
from index import base


def lo(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return base('Hello world!')


app = selector.Selector()
app.add('/resource/{id}', GET=lo)


if __name__ == '__main__':
  httpd = make_server('', 5000, app)
  print "Serving on port 5000..."
  httpd.serve_forever()
