from flask import Flask, render_template,request,send_from_directory,session,flash,redirect
import os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["WAD"]
users = db["users"]
users.create_index("username")


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/upload'

#it's for the session
app.secret_key = "secret key"

    

    
def check_user(username):
    user = users.find_one({"username":username})
    if user :        
       
        return True

def check_password(username,password):
        user=users.find_one({"username":username})
        if user["password"] == password:
            return True

def update_avatar(username,avatar):
         myquery = { "username": username }
         newvalues = { "$set": { "avatar": avatar } }

         users.update_one(myquery, newvalues)
         return True

def get_avatar(username):
        user=users.find_one({"username":username})
        return user["avatar"] 
            

        
@app.route('/', methods=['Get','POST'])
@app.route('/cabinet', methods=['Get','POST'])
def index():
    
      if not session.get('logged_in'):
           return redirect("/login")
      
      else:
        username = session.get('username')   
        
        if request.method == 'POST':
              if request.referrer.endswith('login'):
                  return redirect("/cabinet")
              
              else:
                if 'file' not in request.files:
                      flash('file not exists')
                      return redirect("/cabinet")
                
                if request.files['file'].filename == "":
                      flash('file name is empty')
                      return redirect("/cabinet")
                  
                ff = request.files['file']
                avatar = os.path.join(app.config['UPLOAD_FOLDER'], ff.filename)
                ff.save(avatar)
                update_avatar(username,avatar)
                flash('Successfully saved')
           
        file = get_avatar(username)                      
        return render_template('cabinet.html',file=file)

@app.route('/uploads/<image_name>')
def upload_file(image_name):
       return send_from_directory(app.config['UPLOAD_FOLDER'],image_name)        
          
@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    
    if request.method=='GET':
        session['logged_in'] = False
        return render_template('login.html')   
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if check_user(username):
            if check_password(username, password):
                session['logged_in'] = True
                session['username'] = username
            else :
                flash('Wrong Password!')
        else:
          flash('User not exsit!!')
        return index()

@app.route('/static/<image_name>')
def index2(image_name):
       return send_from_directory('static/upload',image_name)
       

@app.route('/static/<path:path>')
def index3(path):
     return app.send_static_file(path)

  
if __name__ == '__main__':
    
    app.run( port='5000',threaded=True)