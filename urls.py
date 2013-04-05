import json
from server import envey, lo, css, postload, JSON_convert_and_process
from pages import home_page, login_page, logout_page, datapost
from site_css import site_default
from login_stuff import oidapp, db, RecordsYo


SITE_CSS_URL = '/static/site.css'


for page in (home_page, login_page, logout_page):
  page.setdefault('stylesheets', []).append(SITE_CSS_URL)



studyID_to_record_class = {
  'meditrain': RecordsYo,
  }


def process_batch(data):
  record_class = studyID_to_record_class[data['studyID']]
  for record in data['data']:
    record = record_class(**record)
    db.session.add(record)
  db.session.commit()
  return repr(data)


def urls(app):
  app.add('/', GET=envey(PAGE=home_page)(lo))
  post_loader = postload(JSON_convert_and_process(process_batch))(lo)
  app.add('/datapost', POST=envey(PAGE=datapost)(post_loader))
  app.add(SITE_CSS_URL, GET=envey(CSS=site_default)(css))


def logins(app):
  loggy = envey(PAGES=(login_page, logout_page))(oidapp)
  app.add('/log|', GET=loggy, POST=loggy)


everything = [urls, logins]

