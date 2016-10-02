import random
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

# class DormHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template("dorm.html")
#         self.response.write(template)

class BeebeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("beebe.html")
        self.response.write(template.render())

class McAfeeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("mcafee.html")
        self.response.write(template.render())

class TowerHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("tower.html")
        self.response.write(template.render())

class WhoWhyWhatHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("whowhywhat.html")
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/beebe', BeebeHandler),
    ('/mcafee', McAfeeHandler),
    ('/tower', TowerHandler),
    ('/whowhywhat', WhyHandler)
], debug=True)

#help please
