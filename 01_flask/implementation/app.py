from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (Web server gateway interface) application.
'''

### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. I am already liking this course!, looking forward to learning "


@app.route("/index")
def intro():
    return "This is the index page, work in progress!"

if __name__ == "__main__":
    app.run(debug=True)