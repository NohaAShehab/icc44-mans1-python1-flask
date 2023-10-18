

from flask import Flask

# create new flask application
app=  Flask(__name__)  # use flask --app app run


### define your first route
@app.route("/")
def hello_world():
    return "<h1 style='color:red'>Hello, World!</h1>"

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