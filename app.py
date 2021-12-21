from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, AIOps Team!"
def main(): 
    return main.html 
@app.route('/about')
def getAbout():
    return ('welcome to about')

