import os
import selector


app = selector.Selector()
for fn in os.environ['URLS_FILE'].split(':'):
  app.slurp_file(fn.strip())


# URLS_FILE = resource.urls.txt:urls.txt
