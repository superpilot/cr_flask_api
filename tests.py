import datetime
import requests
from requests import async

def main():
  print "hello"
  print datetime.timedelta(minutes=30)
  
  
def get_location():
  #r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
  r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
  print str(r.json["results"][0]["address_components"][3]["long_name"])
  #print str(r.json["results"][0]["formatted_address"])
  #print "location"
  
if __name__ == '__main__':
  #main()
  get_location()