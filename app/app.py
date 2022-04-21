from flask import Flask  

app = Flask(_name_)


@app.route("/home")
def index():
	return "Hello World"

@app.route("/About")
def about():
	return "Hello FROM ABOUT"	

if __name__ == "name":
	app.run(debug =True)

