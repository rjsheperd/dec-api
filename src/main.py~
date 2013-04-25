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
            (r"/user/", UserCreationHandler),
            (r"/user/(\w+)", UserInformationHandler),
            (r"/user/(\w+)/following", UserFollowHandler)
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            db=""
        )
        self.mongo = pymongo.Connection()
        tornado.web.Application.__init__(self, handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello World")


class UserCreationHandler(tornado.web.RequestHandler):

    def post(self):
        # no error checking for now - use WTForms
        first_name = self.get_argument('first_name')
        last_name = self.get_argument('last_name')
        skills = self.get_argument('skills')
        email = self.get_argument('email')
        im = self.get_argument('im')
        bio = self.get_argument('bio')
        user_collection = self.application.mongo.decapi.users

        result = user_collection.insert({
            'first_name': first_name,
            'last_name': last_name,
            'skills': skills,
            'email': email,
            'im': im,
            'bio': bio
        })
        print result
        self.write(json.dumps({"user_id": str(result)}))


class UserInformationHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        result = self.application.mongo.decapi.users.find_one({"_oid": user_id})
        if result is None:
            pass
            #return lookup error
        self.write(json.dumps(result, default=json_util.default))

    def post(self, user_id):
        pass
        #for updating. use WTForms


class UserFollowHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        pass


def main(port='8080', address='localhost'):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
