'''
This is where all the specific content for pages should go.

(Notice that this file/module imports nothing?  Is that significant?)

Both html.py patterns and content (text) can be specified here. The urls.txt
and the pre-made generic structures will compose it properly. (At least
that's the idea.)
'''

#: I'm using this content distribution network.
CDN = 'http://cdnjs.cloudflare.com/ajax/libs/'


def my_ul(c, contents):
  '''
  Wrap the name, text pairs in contents in a UL element.
  The name is put in a SPAN element with the class "heavy" and the text
  gets " - " prepended to it.
  '''
  with c.ul as ul:
    for name, text in contents:
      li = ul.li
      li.span(name.title(), class_='heavy')
      li += ' - ' + text
    return ul


def body(body, title, page_title, form, own_URL):
  '''
  A simple body renderer.
  '''
  body.h1(page_title)
  form(body.div(class_='container'))


def logout_form(c):
  with c.form as f:
    f(action=logout_page['own_URL'], method='POST')
    f.input(value='Logout', type_='submit')
    return f


logout_page = dict(
  stylesheets = ('./static/site.css',),
  title = 'Gazzian Logout',
  page_title = 'Logout',
  body = body,
  form = logout_form,
  own_URL = '/logout',
)
















##page = dict(
##
##  scripts = [CDN + js_lib for js_lib in (
##    'd3/3.0.1/d3.v3.min.js',
##    'underscore.js/1.4.3/underscore-min.js',
##    'jquery/1.8.3/jquery.min.js',
##    'jqueryui/1.9.2/jquery-ui.min.js',
##    )],
##
##  stylesheets = ('http://code.jquery.com/ui/1.9.2/themes/base/jquery-ui.css',),
##
##  body = xerblin_body,
##
##  # The stuff above is used by base() template function, while this stuff
##  # is passed into the body (i.e. xerblin_body above.)
##  title = 'Xerblin',
##  subtitle = 'a Human-Computer Interface',
##  UL = my_ul,
##  things = {
##    'stack': 'a place to put objects for user manipulation. This is similar to a Clipboard but it can hold more than one item at a time. Commands operate on the items on the Stack.',
##    'dictionary': 'a place to keep commands. Any command that is inscribed in the Dictionary can be run from the user interface.',
##    'interpreter': 'a very simple command interpreter that takes care of running commands with the Stack. ',
##    },
##
##)

