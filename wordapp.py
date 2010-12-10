
import cgi 
import os 
import random
import logging


from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api.labs import taskqueue

class ISEEVocabulary(db.Model):
    id= db.IntegerProperty
    wrd = db.StringProperty(multiline=True)
    defn = db.StringProperty(multiline=True)

class MainPage(webapp.RequestHandler):

                                 
    def get(self):

       
        #words=self.init_words() 
        #randid=random.randrange(1,502)
        #resultset = db.GqlQuery("SELECT * FROM ISEEVocabulary")

        #template_values = {
        #   'word':resultset[randid]
        #    }

        #path = os.path.join(os.path.dirname(__file__), 'index.html')
        #self.response.out.write(template.render(path, template_values))

        taskqueue.add(url='/queue', params={})
        path = os.path.join(os.path.dirname(__file__), 'firstpage.html')
        self.response.out.write(template.render(path, {}))

class QueuePage(webapp.RequestHandler):


    def init_words(self):
        f = open('words.txt', 'r')
        for line in f:
            newword=ISEEVocabulary(str(f))
            newword.put();
    
                   
    def post(self):
        words=self.init_words() 

class RepeatPage(webapp.RequestHandler):

    def get(self):

        randid=random.randrange(1,502)
        resultset = db.GqlQuery("SELECT * FROM ISEEVocabulary")
       
        template_values = {
            'word':resultset[randid]
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/more', RepeatPage),
                                      ('/queue', QueuePage),
                                      ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
