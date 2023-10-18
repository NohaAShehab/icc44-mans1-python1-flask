from flask import Flask
from flask import request, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

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
    return (f"<h1 style='color:red; text-align:center'> "
            f"Sorry Requested page Not Found !!!"
            f"{error}"
            f"</h1>")


""" ============= Render template ========"""

students = [{'id': 1, "name": 'Ahmed', 'track': 'python'},
            {'id': 2, "name": 'Abdelrahman', 'track': 'python'},
            {'id': 3, "name": 'Eman', 'track': 'python'},
            {'id': 4, "name": 'Enas', 'track': 'python'}]


@app.route('/landing', endpoint='landing')
def land():
    return render_template('land/landing.html',
                           mycourses=courses, students=students)


@app.route('/landing/<int:id>', endpoint='student.profile')
def student_profile(id):
    filtered_students = list(filter(lambda std: std['id'] == id, students))
    if filtered_students:
        student = filtered_students[0]
        return render_template('land/profile.html', student=student)
    # return 'Not Found', 404
    return render_template('errors/page_not_found.html'), 404


""" Connect to database ====> sqlite """
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)  # this will create instance folder --> contains db


# define db models
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)

    def __str__(self):
        return f"{self.name}"

    def get_image_url(self):
        return  f'students/images/{self.image}'
@app.route('/students/', endpoint='students.index')
def students_index():
    students = Student.query.all()
    return  render_template('students/index.html', students=students)

@app.route('/students/<int:id>', endpoint='students.show')
def student_show(id):
    student = Student.query.get_or_404(id)
    return render_template('students/show.html', student=student)


## create new object
@app.route('/students/create', methods=['GET', 'POST'], endpoint='student.create')
def create():
    if request.method=='POST':
        print(request.form)
        # print("hiiii")
        student = Student(name=request.form['name'], image=request.form['image'])
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students.index'))

    return  render_template('students/create.html' )

# I need to create table
"""
    flask shell
    db.create_all()
"""

# another option to the application
if __name__ == '__main__':
    app.run(debug=True)

# from terminal
"""
    export FLASK_APP=app  
    export DEBUG=True
    to run pp 
    flask run --debug
"""
