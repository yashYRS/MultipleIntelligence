from pprint import pprint
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

global finalscore

app = Flask(__name__,template_folder='templates', static_url_path='/static')
app.secret_key = 'mysecret'

'''english_bot = ChatBot("Chatterbot",
storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = 'chatbot',
                     database_uri = "mongodb://dbUser:dbUser@smartindia-shard-00-00-llgze.mongodb.net:27017,smartindia-shard-00-01-llgze.mongodb.net:27017,smartindia-shard-00-02-llgze.mongodb.net:27017/test?ssl=true&replicaSet=smartindia-shard-0&authSource=admin&retryWrites=true")
'''
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english.greetings")

@app.route('/', methods=['GET','POST'])
def home():
	return render_template('index.html')

@app.route('/score', methods=['GET','POST'])
def score():
	sc = request.form.get('score')
	print("Score: " + str(sc))
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True)
