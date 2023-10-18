from flask import Flask
from flask import request
from flask import render_template
# create new flask application
app = Flask(__name__)  # use flask --app app run


# define your first route
@app.route("/")
def hello_world():
    return "<h1 style='color:red'>Hello, World!</h1>"


@app.route('/request')
def request_info():
    print(f"request is here --> {request}")
    return "<h1 style='color:green; text-align:center'>  This request </h1>"


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


"adding url roles "


def mynewurl():
    return "<h1> Hello form my new url </h1>"

# register function to new url
app.add_url_rule('/newurl', view_func=mynewurl)


"------------ creating new page for 404 not found error---------"
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return  (f"<h1 style='color:red; text-align:center'> "
             f"Sorry Requested page Not Found !!!"
             f"{error}"
             f"</h1>")


""" ============= Render template ========"""

students = [{'id':1, "name":'Ahmed', 'track':'python'},
            {'id':2, "name":'Abdelrahman', 'track':'python'},
            {'id':3, "name":'Eman', 'track':'python'},
            {'id':4, "name":'Enas', 'track':'python'}]
@app.route('/landing')
def land():
    return  render_template('land/landing.html',
                            mycourses=courses, students= students)
@app.route('/landing/<int:id>')
def student_profile(id):
    filtered_students= list(filter(lambda std:std['id']==id, students))
    if filtered_students:
        student = filtered_students[0]
        return render_template('land/profile.html', student=student)
    # return 'Not Found', 404
    return render_template('errors/page_not_found.html'), 404


## another option to the application
if __name__ == '__main__':
    app.run(debug=True)

# from terminal
"""
    export FLASK_APP=app  
    export DEBUG=True
    to run pp 
    flask run --debug
"""
