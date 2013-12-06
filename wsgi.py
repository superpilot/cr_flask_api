from flask import Flask, Request, Response
from blueprint_test import simple_page


application = app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/stories')
#@app.route('/')
#def hello_world():
#    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
    

