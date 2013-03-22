import os
import selector
import urls


app = selector.Selector()
for url in urls.everything:
  url(app)
