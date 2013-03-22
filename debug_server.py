from wsgiref.simple_server import make_server
from main import app


if __name__ == '__main__':
  print "Serving on http://localhost:5000/ ..."
  make_server('', 5000, app).serve_forever()
