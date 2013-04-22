# Python
import os
import json
import random

# Tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web

# PyMongo
import pymongo
from bson import json_util

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/user/", UserCreationHandler)
            ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        self.mongo = pymongo.Connection()
        tornado.web.Application.__init__(self, handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

class UserCreationHandler(tornado.web.RequestHandler):
    def post(self):
        # no error checking for now
        first_name = self.get_argument('first_name')
        last_name = self.get_argument('last_name')
        skills = self.get_argument('skills')

        user_collection = self.application.mongo.decapi.users

        result = user_collection.insert({
                'first_name': first_name,
                'last_name': last_name,
                'skills': skills
                })
        self.write(json.dumps(result, default=json_util.default))

def main(port='8080', address='localhost'):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
