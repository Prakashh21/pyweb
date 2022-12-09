import tornado.web

import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world this is a python command executed from the backend")




if __name__ == "__main__":
    app = tornado.web.Application([
        
        (r"/", basicRequestHandler)
    ])
    
    port  = 8882
    
    app.listen(port)
    
    print(f"application is listening in {port}")
    
    tornado.ioloop.IOLoop.current().start()