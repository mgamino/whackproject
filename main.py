import random
import webapp2
import jinja2
import os
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class DormHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("dorm.html")
        self.response.write(template.render(template_vals))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/dorm', DormHandler)
], debug=True)

#help please
