from server import envey, lo, css
from pages import logout_page
from site_css import site_default


def urls(app):
  app.add('/logout[/]', GET=envey(PAGE=logout_page)(lo))
  app.add('/static/site.css', GET=envey(CSS=site_default)(css))


everything = [urls]
