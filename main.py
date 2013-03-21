import os
import selector


app = selector.Selector()
app.slurp_file(os.environ['URLS_FILE'])
