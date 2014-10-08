# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorators to link the function to a url
@app.route("/")
@app.route("/Hello")

# define the view using a fuciont, which returns a string
def hello_world():
	return "Hello World!"


# start the development server useing the run() method
if __name__ == "__main__":
	app.run()