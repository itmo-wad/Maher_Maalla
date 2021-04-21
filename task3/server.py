from flask import Flask, render_template,request,send_from_directory,session,flash
import re


app = Flask(__name__)

#it's for the session
app.secret_key = "secret key"

#the registered users
logins = {
    'admin':'password'
    }

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
        if "email" not in request.form :
                found=0
                for k,v in logins.items():
                    if request.form['username'] == k:
                        if request.form['password'] == v:
                            session['logged_in'] = True
                            found=1
                            break
                if found ==0 :
                    flash('Wrong Username or Password!')
                return index()    
        else:
             username = request.form.get('username')
             password = request.form.get('password')
             found = 0
             for k,v in logins.items():
                 if username == k :
                     flash('Username aleady exists!')
                     session['logged_in'] = False
                     found = 1
                     return do_reg()
             if found == 0 :
                logins.update( {username : password} )
                session['logged_in'] = True
                return index()
   
@app.route('/static/<image_name>')
def index2(image_name):
       return send_from_directory('static/images',image_name)

@app.route('/static/<path:path>')
def index3(path):
     return app.send_static_file(path)
  
if __name__ == '__main__':

    app.run( port='5000',threaded=True)
