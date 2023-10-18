

from flask import Flask
from flask import request

# create new flask application
app=  Flask(__name__)  # use flask --app app run


### define your first route
@app.route("/")
def hello_world():
    return "<h1 style='color:red'>Hello, World!</h1>"


@app.route('/request')
def request_info():
    print(f"request is here --> {request}")
    return  "<h1 style='color:green; text-align:center'>  This request </h1>"

courses = ['django', 'flask', 'odoo', 'react', 'docker']
@app.route('/courses')
def get_courses():
    return courses

@app.route('/courses/<int:index>')
def get_course(index):
    try:
        return courses[index]
    except:
        return "404"

## another option to the application
if __name__=='__main__':
    app.run(debug=True)

# from terminal
"""
    export FLASK_APP=app  
    export DEBUG=True
    to run pp 
    flask run --debug
"""