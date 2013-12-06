from flask import Blueprint, Response, request, render_template
from pymongo import Connection
import simplejson as json 

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route("/reports/<string:task_id>", methods=["GET"])
def reports(task_id):
    #if request.method == "POST":
    #story = request.GET["story"]
  
    #story = request.Form("story")
    
    client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    db = client["crunchreport-alpha"]
    reports = db.reports
    
    print reports.find()
    
    #reports.insert({"story": "story"})
    json_array = []
    counter = 0
	
    for r in reports.find():
	#print r
	json_array.append({'story' : r["report"]})
	counter += 1
	
    json_response = json.dumps({'results': json_array})
  
    return Response(json_response, status=200, mimetype='application/json')
    
    #return "inserted" + task_id  
    
#@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<story_id>')
def show_story(story_id):
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
    
                        
                        
@simple_page.route('/', defaults={'page': 'index'})
#@simple_page.route('/<page>')
def show_stories(page):
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
    #return page
    
@simple_page.route("/new", methods=["POST"])
def add():
    if request.method == "POST":
	story = request.form["story"]
  
    #story = request.Form("story")
    
    #client = Connection('mongodb://crunchreport-alpha:crunchreport-alpha@paulo.mongohq.com:10001/crunchreport-alpha')
    #db = client["crunchreport-alpha"]
    #reports = db.reports
    
    #reports.insert({"story": "story"})
    
	return "inserted" + story
    
    
@simple_page.route("/template")
def template():
    return render_template('test.html')
 
 
 
 
 
