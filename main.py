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
from professions import category_info
from __init__ import db, create_app


main = Blueprint('main', __name__)
game_agent = GameAgent('game_details.xml')


# #### -------------------- WORD GAMES ---------------------- #####
@main.route('/bullscows', methods=['GET', 'POST'])
def bullscows():
    from Word.BullsAndCows import CowBull
    level = game_agent.curr_level
    if level > 0:
        final_score = CowBull.game_loop(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = CowBull.game_loop(1)
        return redirect(url_for('main.gamelist'))


@main.route('/hangman', methods=['GET', 'POST'])
def hangman():
    from Word.Hangman import hangman
    level = game_agent.curr_level
    if level > 0:
        final_score = hangman.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = hangman.start_game(1)
        return redirect(url_for('main.gamelist'))


# #### -------------------- PICTURE GAMES ---------------------- #####
@main.route('/slidingpuzzle', methods=['GET', 'POST'])
def slidingpuzzle():

    from Picture import sliding_tile
    level = game_agent.curr_level
    if level > 0:
        final_score = sliding_tile.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = sliding_tile.start_game(1)
        return redirect(url_for('main.gamelist'))


# #### -------------------- MUSIC GAMES ---------------------- #####
@main.route('/animal_sound', methods=['GET', 'POST'])
def animal_sound():
    from Music.AnimalSounds import music1
    level = game_agent.curr_level
    if level > 0:
        final_score = music1.start_game()
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = music1.start_game()
        return redirect(url_for('main.gamelist'))


@main.route('/memorymusic', methods=['GET', 'POST'])
def memorymusic():
    from Music.MemoryMusic import memoryMusic
    level = game_agent.curr_level
    if level > 0:
        final_score = memoryMusic.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = memoryMusic.start_game(1)
        return redirect(url_for('main.gamelist'))
# #### -------------------- PEOPLE GAMES ---------------------- #####


@main.route('/people_quiz', methods=['GET', 'POST'])
def people_quiz():
    from People.Quiz import game
    level = game_agent.curr_level
    if level > 0:
        final_score = game.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = game.start_game(1)
        return redirect(url_for('main.gamelist'))

# #### -------------------- SELF GAMES ---------------------- #####


@main.route('/self_quiz', methods=['GET', 'POST'])
def self_quiz():
    from Self.Quiz import game
    level = game_agent.curr_level
    if level > 0:
        final_score = game.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = game.start_game(1)
        return redirect(url_for('main.gamelist'))


# #### -------------------- LOGIC GAMES ---------------------- #####
@main.route('/connect4', methods=['GET', 'POST'])
def connect4():
    from Logic.Connect4 import connect4
    level = game_agent.curr_level
    if level > 0:
        final_score = connect4.start_game(level)
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = connect4.start_game(1)
        return redirect(url_for('main.gamelist'))


# #### -------------------- BODY GAMES ---------------------- #####
@main.route('/spacewars', methods=['GET', 'POST'])
def spacewars():
    from Body.SpaceWars import space_war
    level = game_agent.curr_level
    if level > 0:
        try:
            final_score = space_war.start_game(level)
        except Exception as e:
            final_score = 0
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        try:
            _ = space_war.start_game(1)
        except Exception as e:
            pass
        return redirect(url_for('main.gamelist'))


@main.route('/flappybird', methods=['GET', 'POST'])
def flappybird():
    from Body.FlappyBird import final
    level = game_agent.curr_level
    if level > 0:
        try:
            final_score = final.start_game()
        except Exception as e:
            final_score = 0
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        try:
            _ = final.start_game()
        except Exception as e:
            pass
        return redirect(url_for('main.gamelist'))

# #### -------------------- NATURE GAMES ---------------------- #####


@main.route('/natureqna', methods=['GET', 'POST'])
def natureqna():
    from Nature.Knowledge import nature
    level = game_agent.curr_level
    if level > 0:
        final_score = nature.start_game()
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        _ = nature.start_game()
        return redirect(url_for('main.gamelist'))


@main.route('/natureexplore', methods=['GET', 'POST'])
def natureexplore():
    from Nature.Discover import farmgame
    level = game_agent.curr_level
    if level > 0:
        try:
            final_score = farmgame.start_game()
        except Exception as e:
            final_score = 0
            pass
        game_agent.update_score(final_score)
        next_module, next_game_text = game_agent.get_next_game()
        next_scene = 'main.' + next_module
        return render_template('transition.html',
                               game_text=next_game_text,
                               next_scene=next_scene)
    else:
        try:
            _ = farmgame.start_game()
        except Exception as e:
            pass
        return redirect(url_for('main.gamelist'))

# #### --------------------- START GAME ---------------------- #####


@main.route('/start_game', methods=['GET', 'POST'])
@login_required
def start_game():
    # Create a New Session with user and the session
    new_session = GameSession(current_user.id)
    # add the new session to the database
    db.session.add(new_session)
    db.session.commit()

    game_agent.session_id = new_session
    initial_url = "main.initial_story"

    # Start with the first screen
    return render_template('start_video.html', initial_url=initial_url)


@main.route('/inital_story', methods=['GET', 'POST'])
@login_required
def initial_story():
    # Calculate the maximum possible state for the agent
    game_agent.get_max_states()
    # Reset any data, if available for the agent
    game_agent.reset_curr_state()
    # Create a New Session with user and the session
    game_text = game_agent.get_initial_info()
    # Start with the first screen
    return render_template('transition.html',
                           game_text=game_text,
                           next_scene='main.first_game')


@main.route('/first_game', methods=['GET', 'POST'])
def first_game():
    next_module, next_game_text = game_agent.get_next_game()
    next_scene = 'main.' + next_module
    # Start with the first screen
    return render_template('transition.html',
                           game_text=next_game_text,
                           next_scene=next_scene)


@main.route('/end_game', methods=['GET', 'POST'])
@login_required
def end_game():
    curr_session = game_agent.session_id
    try:
        scores = game_agent.give_final_verdict()

        for category, score in scores.items():
            new_game = SingleGame(category_name=category, score=score, session_id=curr_session)
            db.session.add(new_game)
        db.session.commit()
    except Exception as e:
        pass
    # add the new user to the database
    # Create games objects in database, and store the final score for games
    final_url = "main.profile"
    return render_template('end_video.html', final_url=final_url)


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
        # take the user-supplied password, hash it
        # and compare it to the hashed password in the database
    elif not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('main.login'))
    # if the check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('main.profile'))


@main.route('/transition', methods=['GET', 'POST'])
def transition(game_text="default text", next_scene="gamelist"):
    next_scene = 'main.' + next_scene
    return render_template('transition.html',
                           game_text=game_text,
                           next_scene=next_scene)


# profile page that return 'profile'
@main.route('/profile')
@login_required
def profile():
    max_scores = []
    for curr_item in category_info:
        curr_category = curr_item['category']
        all_games = SingleGame.query.filter_by(category_name=curr_category).all()
        if len(all_games) == 0:
            reqd_score = 0
        else:
            reqd_score = max([game.score for game in all_games])
        curr_item['high_score'] = str(round(reqd_score*100, 2)) + " %"
        max_scores.append(reqd_score)
    max_score = str(round(max(max_scores), 2)) + " %"
    print(max_scores, max_score)
    print([c['high_score'] for c in category_info])

    return render_template('profile.html', name=current_user.name,
                           game_category=category_info, max_score=max_score)


@main.route('/gamelist', methods=['GET', 'POST'])
def gamelist():
    game_agent.session_id = 1
    game_agent.get_max_states()
    game_agent.reset_curr_state()
    game_agent.curr_level = 0
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
