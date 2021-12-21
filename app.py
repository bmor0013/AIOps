from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def getHello():
    return app.send_static_file('main.html')

@app.route('/main')
def getMain():
    return render_template("./main.html")

@app.route('/about')
def getAbout():
    return ('welcome to about')

@app.route("/hello")
def hello():
    return "Hello, AIOps Team!"
