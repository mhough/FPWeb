from server import envey, lo, css
from pages import home_page, login_page, logout_page
from site_css import site_default
from login_stuff import oidapp


SITE_CSS_URL = '/static/site.css'


for page in (home_page, login_page, logout_page):
  page.setdefault('stylesheets', []).append(SITE_CSS_URL)


def urls(app):
  app.add('/', GET=envey(PAGE=home_page)(lo))
  app.add(SITE_CSS_URL, GET=envey(CSS=site_default)(css))


def logins(app):
  loggy = envey(PAGES=(login_page, logout_page))(oidapp)
  app.add('/log|', GET=loggy, POST=loggy)


everything = [urls, logins]

