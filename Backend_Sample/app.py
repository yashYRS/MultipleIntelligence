#import sys
#sys.path.append('/usr/local/lib/python3.6/dist-packages')
import numpy as np
#import detect_blinks
#import spacewars
#import config
#import cv2
from collections import deque
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from pprint import pprint
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__,template_folder='templates', static_url_path='/static')
client = MongoClient("mongodb://dbUser:dbUser@smartindia-shard-00-00-llgze.mongodb.net:27017,smartindia-shard-00-01-llgze.mongodb.net:27017,smartindia-shard-00-02-llgze.mongodb.net:27017/test?ssl=true&replicaSet=smartindia-shard-0&authSource=admin&retryWrites=true")
app.secret_key = 'mysecret'
db = client.Gaming.users

english_bot = ChatBot("Chatterbot",
storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = 'chatbot',
                     database_uri = "mongodb://dbUser:dbUser@smartindia-shard-00-00-llgze.mongodb.net:27017,smartindia-shard-00-01-llgze.mongodb.net:27017,smartindia-shard-00-02-llgze.mongodb.net:27017/test?ssl=true&replicaSet=smartindia-shard-0&authSource=admin&retryWrites=true")

person_bot = ChatBot("Chatterbot",
storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = 'person_bot',
                     database_uri = "mongodb://dbUser:dbUser@smartindia-shard-00-00-llgze.mongodb.net:27017,smartindia-shard-00-01-llgze.mongodb.net:27017,smartindia-shard-00-02-llgze.mongodb.net:27017/test?ssl=true&replicaSet=smartindia-shard-0&authSource=admin&retryWrites=true")



#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english.greetings")
#person_bot.set_trainer(ChatterBotCorpusTrainer)
#person_bot.train("chatterbot.corpus.english")

import threading
import time
finalscore=0
class ThreadingExample(object):

    def __init__(self, interval=1):
        
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            
        thread.start()                                  

    def run(self):
        #detect_blinks.execute()
        #spacewars.executeGame()
        time.sleep(10)
        finalscore=spacewars.levelscore
        time.sleep(self.interval)

def getLog():
	login = session.get('logged_in','')
	l=''
	if login==True:        
		l = 'yes'
	else:
		l='no'
	return l

@app.route('/eyeblink', methods=['GET','POST'])
def eyeblink():
	example = ThreadingExample()
	time.sleep(0)
	return "called"

@app.route('/space', methods=['GET','POST'])
def space():
	example = ThreadingExample()
	time.sleep(0)
	print("FINAL SCORE: "+str(finalscore))
	#print("LevelSCore: "+str(levelscore))
	#pprint("FUNCTION CALLED")
	return render_template('index.html')

@app.route('/game', methods=['POST','GET'])
def game():
	return render_template('index.html')

# multiple chatbots simultaneously. Can be scaled to N
@app.route('/chat1')
def chatbot1():
	return render_template('chat.html')

@app.route('/get')
def get_bot_response():
	userText = request.args.get('msg')
	if 'BYE' in userText.upper():
		return render_template('index.html')
	res = str(english_bot.get_response(userText))
	return str(res)

@app.route('/chat2')
def chatbot2():
	return render_template('chat1.html')

@app.route('/get1')
def get_bot_response1():
	userText = request.args.get('msg')
	if 'BYE' in userText.upper():
		return render_template('index.html')
	res = str(person_bot.get_response(userText))
	return str(res)

## User-specific
@app.route('/',methods=['GET'])
def home():
	return render_template('index1.html')

@app.route('/loginaction',methods=['POST','GET'])
def login():
	number = int(request.form['username'])
	login_user = db.find_one({'Username' : number})
	if login_user:
		if bcrypt.hashpw(request.form['pwd'].encode('utf-8'), login_user['Password']) == login_user['Password']:
			pprint(session['sid'])
			session['logged_in'] = True
			session['username']=number
			l='yes'
			return render_template('index1.html',l=l,name=login_user['First Name'])
		else:
			return "Error"
	else:
		return "Error"

@app.route('/register',methods=['GET','POST'])
def register():
	l=getLog()
	return render_template('register.html', l=l)

@app.route('/registeraction',methods=['GET','POST'])
def registeraction():
	l=getLog()
	existing_user = db.find_one({'Username' : request.form['phn']})
	if existing_user is None:
		fname=request.form.get('fname')
		lname=request.form.get('lname')
		email=request.form.get('email')
		usrn=request.form.get('usrn')
		pwd==request.form.get('pwd')
		rpwd = request.form.get('rpwd')
		if pwd==rpwd:
			hashpass=bcrypt.hashpw(request.form['pwd'].encode('utf-8'), bcrypt.gensalt())
		else:
			return "Passwords don't match!"
		db.insert({"Username": int(usrn), "First Name":fname, "Last Name": lname,"Email": email, "Password": hashpass})
		return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True)
	
