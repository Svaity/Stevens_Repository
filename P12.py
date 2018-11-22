from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/goodbye")
def goodbye():
	return "See ya later"

@app.route("/sample_template")
def template_demo():
	return render_template('parameters.html',
						title="Stevens Repository",
						my_header="My stevens repository",
						my_params="my custom paramerter")

app.run(debug=True)





