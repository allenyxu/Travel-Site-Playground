import data #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  return render_template("home.html", projects=data.setup())

#connects /hello path of server to render hello.html
@app.route('/beach/')
def hello_route():
  return render_template("beach.html", projects=data.setup())

#connects /flask path of server to render flask.html
@app.route('/park/')
def flask_route():
  return render_template("park.html", projects=data.setup())

@app.route('/restaurant/')
def playlist_route():
  return render_template("restaurant.html", projects=data.setup())

@app.route('/videos/')
def video_route():
  return render_template("video.html", projects=data.setup())


if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(debug=True, port='3000', host='0.0.0.0')

