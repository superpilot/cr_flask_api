import datetime
import requests
from requests import async
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import os

def main():
  print "hello"
  print datetime.timedelta(minutes=30)
  
  
def get_location():
  #r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
  r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
  print str(r.json["results"][0]["address_components"][3]["long_name"])
  #print str(r.json["results"][0]["formatted_address"])
  #print "location"
  
  
def test():
    #    return s.dumps({ 'id': self.id })
  a = os.urandom(64)
  #print(a.encode('base-64'))
  s = Serializer(a)
  print s.dumps({"id": "id"})
  #uuid
    
if __name__ == '__main__':
  #main()
  test()
     