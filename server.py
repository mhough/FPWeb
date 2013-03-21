from wsgiref.simple_server import make_server
import selector
from index import base, my_ul

def g(body, title, **a):
  body.h1(title)
  my_ul(body, a.get('contents', {}).iteritems())

def lo(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return base('Hello world!', body=g, contents = {
      'stack': 'a place to put objects for user manipulation. This is similar to a Clipboard but it can hold more than one item at a time. Commands operate on the items on the Stack.',
      'dictionary': 'a place to keep commands. Any command that is inscribed in the Dictionary can be run from the user interface.',
      'interpreter': 'a very simple command interpreter that takes care of running commands with the Stack. ',
      },
                )




app = selector.Selector()
app.add('/resource/{id}', GET=lo)


if __name__ == '__main__':
  httpd = make_server('', 5000, app)
  print "Serving on port 5000..."
  httpd.serve_forever()
