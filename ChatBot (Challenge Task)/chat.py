from flask import Flask, render_template,request
import re

app = Flask(__name__)



@app.route('/', methods=['Get','POST'])
def index():
      
      msg=''
 # get the message from the user from the attribute name: 'message' and get the whole dialog from the attribute 'messages'     
      if request.method == 'POST':
          getdata = request.form.get("message")
          msg = request.form.get("messages")
          
          user = 'Me : '+ getdata + '\n'
          
          msg = msg + user
		#defining a key/value dictionary to be used as a re-defined answers from the Bot, 
		#we will search inside it usinf ReqEx and try to fine the suitable answer
          keywords = {
              
              'Hello.\n  How are you ?':['.*hello.*','^hi$','.*good morning.*','.*good afternoon.*','.*good evening.*'],
			  'My name is Michael).\n':['.*your name.*','.*name.*'],
              'I am fine.': ['.*how are you.*'],
			  'well, i guess I was created the moment you run this app, so a little young I guess)': ['.*old.*','.*age.*','.*birth.*'],
              'you are welcome.':['.*thank.*'],
              'Goodbye':['.*bye.*']

           }
          # search in the dictionary and try to find a suitable answer by usinf reqular expressions
          found = 0
          bot = 'Bot: '
          for key,value in keywords.items():
              rr = re.compile('|'.join(value),re.IGNORECASE)
              if re.search(rr, getdata):
                  bot = bot + key + '\n'
                  found = 1
                  break
         #default msg  
          if found == 0 :
                 bot = bot+ 'Sorry, did not get it(\n'
                 
          msg = msg + bot + '\n'         
                   
      return render_template('index.html',dialog=msg)
      

   
if __name__ == '__main__':

    app.run( port='5000',threaded=True)
