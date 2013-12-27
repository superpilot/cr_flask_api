from flask import Blueprint, Response, request, render_template
from pymongo import Connection, GEO2D
from bson.objectid import ObjectId
import simplejson as json 
import datetime
from bson.son import SON
import requests

simple_page = Blueprint('crunchreport', __name__,
                        template_folder='templates')


@simple_page.route("/<string:story_id>/reports/", methods=["GET", "POST"])
def reports(story_id):
    #if request.method == "POST":
    #story = request.GET["story"]
  
    #story = request.Form("story")
    
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    reports = db.reports
    
    print story_id
    
    reports = reports.find({"story_id": ObjectId(story_id)})
    
    #reports.insert({"story": "story"})
    json_array = []
    counter = 0
	
    for r in reports:
	#print r
	json_array.append({'story' : r["report"], "report_date": r["datetime"]})
	counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    
    #return "inserted" + task_id  
    
#@simple_page.route('/', defaults={'page': 'index'})
#@simple_page.route('/<story_id>')
#def get_story_data(story_id):
#    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
#    db = client["crunchreport-alpha"]
#    stories = db["top_stories"]
    
#    print stories.find()
    
#    json_array = []
#    counter = 0
	
#    for r in stories.find():
#	json_array.append({'story' : r["story"]})
	#counter += 1
	
#    json_response = json.dumps({'results': json_array})
  
#    return Response(json_response, status=200, mimetype='application/json')
    
    
                        
#@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/comments')
def show_story_comments(page):
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories = db["top_stories"]
    
    print stories.find()
    
    json_array = []
    counter = 0
	
    for r in stories.find():
	json_array.append({'story' : r["story"]})
	#counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    
                        
                        
@simple_page.route('/local', methods=["POST", "GET"])
#@simple_page.route('/<page>')
def local_stories():
  
    #latitude = request.form["latitude"]
    #longitude = request.form["longitude"]
    #datetime = request.forn["datetime"]
  
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories_collection = db["stories"]
    
    results = stories_collection.find({})
    #results = stories_collection.find({'datetime': {'$gte': str(thirty_minutes_ago)}, 'keywords': {'$in': ["monkee"]}, 'coords': SON([('$near', [1, 1]), ('$maxDistance', 20)])})
	    
    #db.places.create_index([("loc", GEO2D)])
    #results = db.command(SON([('geoNear', 'stories'), ('near', [1, 2]), ('query', {'keyword': {'$in': ['monkee']})]))
	
    
    json_array = []
    counter = 0
	
    for r in results:
	json_array.append({"story_id": str(r["_id"]), 'story' : " ".join(r["keywords"]), "last_report": r["last_report"], "report_count": r["report_count"]})
	#counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    #return page
    #r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
    #print str(r.json["results"]["formatted_address"])
    #return Response("here")
    
    
@simple_page.route('/county', methods=["POST", "GET"])
#@simple_page.route('/<page>')
def county():
  
    #county = request.form["county"]
    #longitude = request.form["longitude"]
    #datetime = request.forn["datetime"]
    
    r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
    county = str(r.json["results"][0]["address_components"][3]["long_name"])
	
  
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories_collection = db["stories"]
    
    results = stories_collection.find({"county": "Los Angeles"})
    #results = stories_collection.find({'datetime': {'$gte': str(thirty_minutes_ago)}, 'keywords': {'$in': ["monkee"]}, 'coords': SON([('$near', [1, 1]), ('$maxDistance', 20)])})
	    
    #db.places.create_index([("loc", GEO2D)])
    #results = db.command(SON([('geoNear', 'stories'), ('near', [1, 2]), ('query', {'keyword': {'$in': ['monkee']})]))
	
    
    json_array = []
    counter = 0
	
    for r in results:
	json_array.append({"story_id": str(r["_id"]), 'story' : r["story"], "last_report": r["last_report"], "report_count": r["report_count"]})
	#counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    #return page
    #r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
    #print str(r.json["results"]["formatted_address"])
    #return Response("here")
    
    
@simple_page.route('/state', methods=["POST", "GET"])
#@simple_page.route('/<page>')
def state():
  
    #county = request.form["county"]
    #longitude = request.form["longitude"]
    #datetime = request.forn["datetime"]
  
    r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
    state = str(r.json["results"][0]["address_components"][4]["long_name"])
	    
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories_collection = db["stories"]
    
    results = stories_collection.find({"state": "CA"})
    #results = stories_collection.find({'datetime': {'$gte': str(thirty_minutes_ago)}, 'keywords': {'$in': ["monkee"]}, 'coords': SON([('$near', [1, 1]), ('$maxDistance', 20)])})
	    
    #db.places.create_index([("loc", GEO2D)])
    #results = db.command(SON([('geoNear', 'stories'), ('near', [1, 2]), ('query', {'keyword': {'$in': ['monkee']})]))
	
    
    json_array = []
    counter = 0
	
    for r in results:
	json_array.append({"story_id": str(r["_id"]), 'story' : r["story"], "last_report": r["last_report"], "report_count": r["report_count"]})
	#counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    #return page
    #r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
    #print str(r.json["results"]["formatted_address"])
    #return Response("here")
    
    
@simple_page.route("/reports/new", methods=["POST"])
def add():
    if request.method == "POST":
	report = request.form["report"]
	report_datetime = request.form["datetime"]
	#latitude = request.form["latitude"]
	#longitude = request.form["longitude"]
  
	#story = request.Form("story")
	
	client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
	db = client["crunchreport-alpha"]
	reports_collection = db.reports
	stories_collection = db.stories
	
	
	#reports.insert({"story": "story"})
	report_split = report.split(" ")
	#print type(report_split)
	keywords_array = []
	story_title = " ".join(report_split)
	stop_words_list = ["a", "on", "the", "of", "that", "and", "theres"]
	for word in report_split:
	    if word not in stop_words_list:
		keywords_array.append(word)
		#story_title += word 
		
	#print keywords_array[0]
	#print datetime.datetime.utcnow()	
	#add report to story
	reports_collection.create_index([("coords", GEO2D)])
	#reports = reports_collection.insert({'report': report,  'datetime': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), 'coords': [1,1], 'keywords': ["monkee"]})
	#reports = reports_collection.insert({'report': report,  'datetime': datetime, 'coords': [1,1], 'keywords': ["monkee"]})
	#reports = reports_collection.insert({'report': "report",  'datetime': "2013-12-15 16:35", 'coords': [1,1], 'keywords': ["monkee"]})
	#print reports	
	
	#results = reports_collection.find({}).limit(2)
	
	#thirty_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
	thirty_minutes_ago = datetime.datetime.strptime(report_datetime, "%Y-%m-%d %H:%M") - datetime.timedelta(minutes=30)
	print "30again" + str(thirty_minutes_ago)
	
	reports = reports_collection.find({'datetime': {'$gte': str(thirty_minutes_ago)}, 'keywords': {'$in': keywords_array}, 'coords': SON([('$near', [1, 1]), ('$maxDistance', 20)])})
	reports_count = reports.count()
	#print "count" + str(reports.count())
	print "count" + str(reports_count)
	
	#objectids_list = []
	#for r in results:
	#  print r["_id"]
	
		
	
	#results = db.command(SON([('geoNear', 'reports'), ('near', [1, 1]), ('query', {'keywords': {'$in': ['monkee']}})]))
	#print results
	#now = datetime.datetime.utcnow()
	#now_string = str(now.year) + " " + str(now.month) + " " + str(now.day) + " " + str(now.hour) + " " + str(now.minute) 
	#print "now" + str(now)
		
	
	if reports.count() == 0:
	  #reports = reports_collection.insert({'report':  report,  'datetime': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), 'coords': [1,1], 'keywords': ["monkee"]})
	  reports = reports_collection.insert({'report':  report,  'datetime': report_datetime, 'coords': [1,1], 'keywords': keywords_array})
	
	elif reports.count() == 1:
	    #story = stories_collection.insert({'story': str(keywords_array),  'last_report': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), 'coords': [1,1], 'keywords': ["monkee"]})
	    story = stories_collection.insert({'story': story_title,  'last_report': report_datetime, 'coords': [1,1], 'report_count': 2})
	    #reports = reports_collection.insert({'story_id': story, 'report': "test",  'datetime': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), 'coords': [1,1], 'keywords': ["monkee"]})
	    reports_collection.insert({'story_id': story, 'report': report,  'datetime': report_datetime, 'coords': [1,1], 'keywords': keywords_array})
	  	  
	    for r in reports:
	        reports_collection.update({"_id": r["_id"]}, {"$set": {"story_id": story}})
	    
	elif reports.count() > 1:
	    print "count > 3"
	    story_id = ""
	    count = 0
	    for r in reports:
		print r["_id"]
	        if count == 0:
		  story_id = str(r["story_id"])
		  #reports_collection.update({"_id": r["_id"]}, {"$set": {"story_id": story}})
	    #print "storyid" + str(ObjectId(story_id))
	    #print str(datetime.datetime.strptime("2013-12-15 7:30", "%Y-%m-%d %H:%M"))
	    reports = reports_collection.insert({'story_id': ObjectId(story_id), 'report': report,  'datetime': report_datetime, 'coords': [1,1], 'keywords': ["monkee"]})
	    stories_collection.update({"story_id": ObjectId("story_id")}, {"report_count": {"$inc": 1}})
	    
	
	
	
	#if reports.count is larger then 1
	#report_count = len(results["results"])
	#add the report including the story id
	##for r in reports:
	#  print "here" + str(r)
	#  objectids_list.append(r["_id"]
	#  if counter = 0:
	#	story_id = r["story_id"]
	#	break
	##reports_collection.insert({"report": "report", "keywords": "keyords", "datetime": "datetime", "story_id": "story_id"})
	#get story_id of first record
	#update record cound of story record
	#stories_collection.update({"datetime": "datetime"}, {"$inc": {"report_count": 1}})
	
	
	
	
	
	#if count == 0
	#just add the report
	
	
	
	#for r in results:
	#  if round(((now - datetime.datetime.strptime(r["datetime"], "%Y-%m-%d %H:%M:%S")).total_seconds()/60)) < 15:
	#    print "yes"
	
	
	#for r in results["results"]:
	#  print str(now) + " " + str(r["obj"]["datetime"])
	#  if now.year == r["obj"]["datetime"].year and now.month == r["obj"]["datetime"].month and now.day == r["obj"]["datetime"].day and now.hour == r["obj"]["datetime"].hour:
	#    print now.minute - r["obj"]["datetime"].minute
	#    if now.minute - r["obj"]["datetime"].minute < 30:
	      #just save objectids
	#      objectids_list.append(r["obj"]["_id"])
	#      print "added to objectids list"  
	      #else:
	      #add the report
	    #  print "added report"	      
	      
	#print len(objectids_list)
	#if count objectids == 0
	#just ad report
	#if count objects ids == 1
	#create story and set reports story id to that
	#update stories report count and last reported time
	#if count larger then 1 then update story report count and last seen time
	#count = count + 1
	      
	      
	  
	  #string_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
	  #print r["obj"]["datetime"] - datetime.datetime.now()
	  #print string_date
	  
	#print "time" + str((datetime.datetime.now() - datetime.timedelta(minutes=15)).total_seconds())
	#t1 = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
	#t2 = datetime.datetime.strptime(str(datetime.datetime.now() - datetime.timedelta(minutes=15)), "%Y-%m-%d %H:%M:%S.%f")
	#print str(((t1-t2).seconds/60))
	#print str(datetime.datetime.now() - datetime.timedelta(minutes=15))
	
	#if no stories match tags then just insert
	#if one report exists then create a stroy with the tags from the reports set report number to 2
	#set storyid to the storyid
	#set title to tags of first report
	#if more then 2 then update the time of the last report
	
	
	#report.replace("the", "")
	#report.replace("of", "")
	#report.replace("that", "")
	
	return "inserted" + str(keywords_array)
    
    
    
@simple_page.route("/reports/star/new", methods=["POST"])
def add_star():
    #client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    #db = client["crunchreport-alpha"]
    #reports = db.reports
	
    #reports.update({"story": "story"})
    #reports.update({'_id':p['_id']},{'$inc':{'star': 1}},upsert=False, multi=False)
    
    
    
    
    return Response({"added": "added"}, status=200, mimetype='application/json')
    
    
@simple_page.route('/top', defaults={'page': 'index'})
#@simple_page.route('/<page>')
def top_stories(page):
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories_collection = db["stories"]
    
    #find stories with most reports
    
    #print stories.find()
    
    #db.places.create_index([("loc", GEO2D)])
    #results = db.command(SON([('geoNear', 'stories'), ('near', [1, 2]), ('query', {'keyword': {'$in': ['monkee']})]))
	
    
    json_array = []
    counter = 0
	
    for r in results.find():
	json_array.append({'story' : r["story"]})
	#counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    #return page
    
    
@simple_page.route("/template")
def template():
    return render_template('test.html')
    
@simple_page.route("/reports/new1", methods=["POST"])
def add1():
  
    report = request.form["report"]
    #report_datetime = request.form["datetime"]
    #latitude = request.form["latitude"]
    #longitude = request.form["longitude"]
    
    report_split = report.split(" ")
    keywords_array = []
    
    stop_words_list = ["a", "on", "the", "of", "that", "and", "theres"]
    for word in report_split:
	if word not in stop_words_list:
	    keywords_array.append(word)
	
	
    #thirty_minutes_ago = datetime.datetime.strptime(report_datetime, "%Y-%m-%d %H:%M") - datetime.timedelta(minutes=30)
    #print "30again" + str(thirty_minutes_ago)
    
  
    #check stories collection to see if one exists with parameters
    #if it doesnt create one set report count to 1 and create a report
    
    #if  it does and report count is 1 then increment and update the gps and addtoset the tags and create the report
    
    #when searching look for stories with report count > 1
    
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    stories_collection = db["stories"]
    reports_collection = db["reports"]
 
    #reports_collection.create_index([("coords", GEO2D)])
 
    #stories = stories_collection.find({'datetime': {'$gte': str(thirty_minutes_ago)}, 'keywords': {'$in': keywords_array}, 'coords': SON([('$near', [1, 1]), ('$maxDistance', 20)])})
    stories = stories_collection.find({"keywords": {"$in": ["monkeeys"]}})
    stories_count = stories.count()
    
    if stories_count == 0:
	#get county/state
	# r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=53.244921,-2.479539&sensor=true')
	#print str(r.json["results"][0]["address_components"][3])
	#print str(r.json["results"][0]["formatted_address"])
	
	r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
	county = str(r.json["results"][0]["address_components"][3]["long_name"])
	state = str(r.json["results"][0]["address_components"][4]["long_name"])
		
	story_id = stories_collection.insert({"coords": [1, 1], "keywords": ["monkeeys"], "report_count": 0, "last_report_datetime": "2013-12-12"})
	print story_id
	#report_collection.insert()
	
	#json_response = json.dumps({'results': json_array})
	
	return Response("json_response", status=200, mimetype='application/json')
    	
    elif stories_count > 0:
	r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=34.2437,-118.2437&sensor=true")
	county = str(r.json["results"][0]["address_components"][3]["long_name"])
	state = str(r.json["results"][0]["address_components"][4]["long_name"])
	#print county
	
	#get story id
	#if county != "":
	stories_collection.update({"_id": ObjectId("52bcd3a05f655547c1e54d76")}, {"$inc": {"report_count": 1}, "$addToSet": {"keywords": { "$each": ["lions", "tigers"]}}, "$set": {"coords": [3, 3], "county": county, "state": state, "last_report_datetime": "2013-12-12"}})
	#report_collection.insert()
	#stories_collection.update({"_id": ObjectId("52bcd3a05f655547c1e54d76")}, {"$set": {"county": "county"}})
	
	return Response("json_response", status=200, mimetype='application/json')
    
	
 
 
 
 
 
