from wsgiref.simple_server import make_server
import selector


if __name__ == '__main__':
  s = selector.Selector()
  s.slurp_file('urls.txt')
  
  httpd = make_server('', 5000, s)
  print "Serving on http://localhost:5000/ ..."
  httpd.serve_forever()
