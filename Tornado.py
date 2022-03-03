import tornado.ioloop
import tornado.web
from datetime import datetime
from time import sleep
import random
from statistics import mean

#Create index page handler
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

#Create page for single weather reading (getOne.html)
class WeatherOne(tornado.web.tornado.web.RequestHandler):
    def get(self):
        tempin = str(random.randint(-20, 100))
        humin = str(random.randint(0, 100))
        now = datetime.now()
        timein = str(now.strftime("%H:%M:%S"))
        self.render("getOne.html", tempin=tempin, humin=humin, timein=timein)

#Create page for single weather reading (getTen.html)
class WeatherTen(tornado.web.tornado.web.RequestHandler):
    def get(self):
        #Initialize arrays to store temp/humidity data
        t=[]
        h=[]
        n=[]
        #Read in ten values from pseudosensor
        for i in range(10):    
            tempin = str(random.randint(-20, 100))
            t.append(int(tempin))
            humin = str(random.randint(0, 100))
            h.append(int(humin))
            now = datetime.now()
            timein = str(now.strftime("%H:%M:%S"))
            n.append(timein)
            sleep(1)
        #Calculate statistics    
        tsum=sum(t)
        tlen=len(t)
        avgt=tsum/tlen
        hsum=sum(h)
        hlen=len(h)
        avgh=hsum/hlen
        maxt=max(t)
        mint=min(t)
        maxh=max(h)
        minh=min(h)
        self.render("getTen.html", t=t, maxt=maxt, mint=mint, avgt=avgt, h=h, maxh=maxh, minh=minh, avgh=avgh, n=n)

app = tornado.web.Application([
    (r"/",IndexHandler),
    (r"/getoneweatherplease", WeatherOne),
    (r"/gettenweathers", WeatherTen)
])

app.listen(8080)
tornado.ioloop.IOLoop.current().start()