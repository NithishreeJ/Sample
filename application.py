from flask import Flask
application = Flask(__name__) 
app=application
  
@application.route("/")
def home():
    return "Hello From Nithi Shree"
  
if --name--=="--main--"
     application.run(debug="true")
  
