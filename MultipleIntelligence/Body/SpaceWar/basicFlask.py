from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import pymongo
from pprint import pprint
from datetime import datetime
import png
import os
import random
import bson
from bson import ObjectId
import bcrypt
from werkzeug import secure_filename
from gridfs import GridFS
from gridfs.errors import NoFile
from flask import Flask,flash, redirect, render_template, send_file,request, session, make_response, abort, url_for

app = Flask(__name__, template_folder='template',  static_url_path='/static')
'''
@app.route('/',methods=['GET','POST'])
def func1():
	Code here
	return render_template('tem1.html',args=args)
	OR
	return redirect(url_for('func_name'))'''

if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True)
	
