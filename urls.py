from server import envey, lo, css
from pages import login_page, logout_page
from site_css import site_default


SITE_CSS_URL = '/static/site.css'


login_page.setdefault('stylesheets', []).append(SITE_CSS_URL)
logout_page.setdefault('stylesheets', []).append(SITE_CSS_URL)


def urls(app):
  app.add(login_page['own_URL'] + '[/]', GET=envey(PAGE=login_page)(lo))
  app.add(logout_page['own_URL'] + '[/]', GET=envey(PAGE=logout_page)(lo))
  app.add(SITE_CSS_URL, GET=envey(CSS=site_default)(css))


everything = [urls]
