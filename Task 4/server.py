from flask import Flask, render_template,request,send_from_directory,session,flash
import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["WAD"]
users = db.users


app = Flask(__name__)


#it's for the session
app.secret_key = "secret key"


    
def check_user(username):
    user = users.find_one({"username":username})
    if user :        
       
        return True

def check_pass(username,password):
        user=users.find_one({"username":username,"password":password})
        if user:
            return True

        
@app.route('/', methods=['Get','POST'])
@app.route('/cabinet', methods=['Get','POST'])
def index():

    
      if not session.get('logged_in'):
          return render_template('login.html')
      
      else:

        return render_template('cabinet.html')
                 
@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method=='GET':
        session['logged_in'] = False
        return index()  
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if check_user(username):
                    if check_pass(username, password):
                        session['logged_in'] = True
                    else :
                        flash('Wrong Password!')
        else:
          flash('User not exsit!!')
        return index()    

     
@app.route('/static/<image_name>')
def index2(image_name):
       return send_from_directory('static/images',image_name)
       

@app.route('/static/<path:path>')
def index3(path):
     return app.send_static_file(path)
	 

if __name__ == '__main__':
    
    app.run( port='5000',threaded=True)
