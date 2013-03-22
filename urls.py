from server import envey, lo, css
from pages import home_page, login_page, logout_page
from site_css import site_default


SITE_CSS_URL = '/static/site.css'


for page in (home_page, login_page, logout_page):
  page.setdefault('stylesheets', []).append(SITE_CSS_URL)


def urls(app):
  app.add('/', GET=envey(PAGE=home_page)(lo))
  app.add(SITE_CSS_URL, GET=envey(CSS=site_default)(css))


def login(app):
  app.add(login_page['own_URL'] + '[/]', GET=envey(PAGE=login_page)(lo))
  app.add(logout_page['own_URL'] + '[/]', GET=envey(PAGE=logout_page)(lo))


everything = [urls, login]
