    # Python
import os
import json
import random

# Tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", HomeHandler),(r"/voet/(\w+)", VoetHandler)
            ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
        self.write("Hello World\n")
class VoetHandler(tornado.web.RequestHandler):
	def get(self, input):
		temp = input
		scramble = ""
		while len(temp) > 0:
			i = random.randint(0,len(temp)-1)
			scramble = scramble + temp[i]
			temp = temp[:i]+temp[i+1:]
		self.write("<h1>Alex Voet</h1><br>To be scrambled: " + input + "<br> Scrambled: " + scramble + "\n")

def main(port='8080', address='localhost'):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
