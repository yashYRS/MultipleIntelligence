import sys
import random

from pprint import pprint

import xml.etree.ElementTree as ET

from flask import Flask, Blueprint, render_template, request
from flask import jsonify, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import UserMixin
from models import User, GameSession, SingleGame


from Game import GameAgent
from __init__ import db, create_app


main = Blueprint('main', __name__)


@main.route('/call', methods=['GET', 'POST'])
def call():
    pprint("Session Score: " + str(session['finalscore']))
    game = callai()
    pprint("Game Selected by AI: " + str(game))
    return render_template('Screens.html', game=game)


def callai():
    game = ai(float(session['finalscore']))
    return game


# #### -------------------- WORD GAMES ---------------------- #####
@main.route('/bullscows', methods=['GET', 'POST'])
def bullscows():
    from Word.BullsAndCows import CowBull
    level = int(request.form.get('level'))
    finalscore = CowBull.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint("Bulls:" + str(finalscore))
    return "1"


@main.route('/hangman', methods=['GET', 'POST'])
def hangman():
    from Word.Hangman import hangman
    level = int(request.form.get('level'))
    finalscore = hangman.mainloop(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint("Hangman:" + str(finalscore))
    return "1"


# #### -------------------- PICTURE GAMES ---------------------- #####
@main.route('/slidingpuzzle', methods=['GET', 'POST'])
def slidingpuzzle():

    level = int(request.form.get('level'))
    filepath = './pictures'
    if level == 1:
        from Picture.SlidingPuzzle import slidingpuzzle_1
        finalscore = slidingpuzzle_1.start_game(filepath)
    elif level == 2:
        from Picture.SlidingPuzzle import slidingpuzzle_2
        finalscore = slidingpuzzle_2.start_game(filepath)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


# #### -------------------- MUSIC GAMES ---------------------- #####
@main.route('/animalsound', methods=['GET', 'POST'])
def animalsound():
    from Music.AnimalSounds import music1
    music1.start_game()
    print("In animalsound")
    finalscore = 0
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    return "1"


@main.route('/memorymusic', methods=['GET', 'POST'])
def memorymusic():
    from Music.MemoryMusic import memoryMusic
    level = int(request.form.get('level'))
    finalscore = memoryMusic.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


@main.route('/isometric1', methods=['GET', 'POST'])
def isometric1():
    return render_template('indexN1.html')


@main.route('/isometricscore', methods=['GET', 'POST'])
def isometricscore():
    sc = request.form.get('score')
    print("Score: " + str(sc))
    session['finalscore'] = sc
    return "1"


@main.route('/isometric2', methods=['GET', 'POST'])
def isometric2():
    return render_template('indexN2.html')


# #### -------------------- PEOPLE GAMES ---------------------- #####

@main.route('/people_quiz', methods=['GET', 'POST'])
def people_quiz():
    from People.Quiz import game
    finalscore = 0
    level = int(request.form.get('level'))
    game.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("People Quiz: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"

# #### -------------------- SELF GAMES ---------------------- #####


@main.route('/self_quiz', methods=['GET', 'POST'])
def self_quiz():
    from Self.Quiz import game
    finalscore = 0
    level = int(request.form.get('level'))
    game.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Connect4: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


# #### -------------------- LOGIC GAMES ---------------------- #####
@main.route('/connect4', methods=['GET', 'POST'])
def connect4():
    from Logic.Connect4 import connect4
    finalscore = 0
    level = int(request.form.get('level'))
    connect4.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Connect4: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


# #### -------------------- BODY GAMES ---------------------- #####
@main.route('/spacewars', methods=['GET', 'POST'])
def spacewars():
    # ## TO DO ###
    from Body.SpaceWar import spacewars1
    finalscore = 0
    level = int(request.form.get('level'))
    spacewars1.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Spacewars: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


@main.route('/flaapybird', methods=['GET', 'POST'])
def flappybird():
    # ## TO DO ###
    from Body.FlappyBird import game
    finalscore = 0
    level = int(request.form.get('level'))
    game.start_game()
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Spacewars: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"

# #### -------------------- NATURE GAMES ---------------------- #####


@main.route('/natureqna', methods=['GET', 'POST'])
def natureqna():
    from Nature.Knowledge import nature
    finalscore = 0
    level = int(request.form.get('level'))
    nature.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("NatureQNA" + str(level) + ": " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


@main.route('/natureexplore', methods=['GET', 'POST'])
def natureexplore():
    from Nature.Discover import farmgame
    farmgame.start_game()
    # level = int(request.form.get('level'))
    finalscore = natureexplore.start_game()
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


# #### --------------------- START GAME ---------------------- #####

@main.route('/start_game', methods=['GET', 'POST'])
@login_required
def start_game():
    # Create a New Session with user and the session
    # Create a Agent
    # Start with the first screen
    return render_template('FirstScreen.html', game=game, l=lvalue)


# #### --------------------- LOG-IN & REGISTER ---------------------- #####
@main.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in', False):
        redirect(url_for('main.profile'))
    return render_template('login.html')


@main.route('/loginaction', methods=['POST', 'GET'])
def loginaction():

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    # check if the user actually exists
    if not user:
        flash('Please sign up before!')
        return redirect(url_for('main.login'))
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
    elif not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('main.login'))
    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('main.profile'))


# profile page that return 'profile'
@main.route('/profile')
# @login_required
def profile():
    category_info = [
        {
            'category': 'Word',
            'photo': '/static/images/Word.jpeg',
            'game_list': ['Bulls And Cows', 'Hangman']
        },
        {
            'category': 'Logic',
            'photo': '/static/images/Logic.jpeg',
            'game_list': ['Connect4']
        },
        {
            'category': 'Self',
            'photo': '/static/images/Self.jpeg',
            'game_list': ['Self Quiz']
        },
        {
            'category': 'People',
            'photo': '/static/images/People.jpeg',
            'game_list': ['People Quiz']
        },
        {
            'category': 'Picture',
            'photo': '/static/images/Picture.jpeg',
            'game_list': ['Sliding Puzzle']
        },
        {
            'category': 'Nature',
            'photo': '/static/images/Nature.jpeg',
            'game_list': ['Nature Explore', 'Nature Q&A']
        },
        {
            'category': 'Music',
            'photo': '/static/images/Music.jpeg',
            'game_list': ['Memory Music']
        },
        {
            'category': 'Body',
            'photo': '/static/images/Body.png',
            'game_list': ['Flappy Bird', 'Space Wars']
        },
    ]
    return render_template('profile.html', name=current_user.name,
                           game_category=category_info)


@main.route('/gamelist', methods=['GET', 'POST'])
def gamelist():
    return render_template('gamelist.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@main.route('/registeraction', methods=['GET', 'POST'])
def registeraction():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('pwd')
    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()
    # If user is found, try to sign in again
    if user:
        flash('Email address already exists')
        return redirect(url_for('main.login'))
    # create a new user with the form data with hashed password
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.login'))


@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


app = create_app()
if __name__ == '__main__':
    # create the SQLite database
    db.create_all(app=create_app())
    app.run(host='127.0.0.1', debug=True)
