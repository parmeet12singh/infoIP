from datetime import datetime
import pytz

class infoIP():
    def __init__(self, ip, city, state, country, address, postal, lat, lng, org, timezone, flag=None):

        self.ip = ip
        self.city = city
        self.state = state
        self.country = country
        self.address = address
        self.postal = postal
        self.flag = "https://flagcdn.com/w320/"+country.lower()+".png"
        self.lat = lat
        self.lng = lng
        self.org = org
        self.date = datetime.now(pytz.timezone(timezone)).strftime("%x")
        self.time = datetime.now(pytz.timezone(timezone)).strftime("%X")
        self.timezone = timezone