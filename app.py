from flask import Flask, request,render_template
app = Flask(__name__)



@app.route('/', methods = ["POST","GET"])
def getHello():
    if request.method == 'POST':
        user = request.form["entry"]
        return(str(user))        
    else:
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
