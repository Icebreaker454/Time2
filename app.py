import tornado.ioloop
import tornado.web

from settings import settings


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')


class TimerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('timer.html')


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/about', AboutHandler),
        (r'/timer', TimerHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
