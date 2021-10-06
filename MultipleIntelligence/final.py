import sys
import random
from pprint import pprint
import xml.etree.ElementTree as ET
from pymongo import MongoClient
from flask import Flask, render_template, request
from flask import jsonify, redirect, url_for, session


# ###  --------------  GLOBAL VARIABLES -------- -  ####

global finalscore
alpha = 0.7
beta = 0.3
thld_one = 0.9
thld_common = 0.4
games_played = 0
filename = "temp_game_details.xml"
curr_state = {}
curr_score = {}
maximum_state = {
    "self": 0,
    "word": 0,
    "body": 0,
    "music": 0,
    "logic": 0,
    "nature": 0,
    "people": 0,
    "picture": 0
    }

levels_per_game = []
levels_done = []
games_limit = 10


app = Flask(__name__, template_folder='templates', static_url_path='/static')
client = MongoClient("mongodb://dbUser:dbUser@smartindia-shard-00-00-llgze.mongodb.net:27017,smartindia-shard-00-01-llgze.mongodb.net:27017,smartindia-shard-00-02-llgze.mongodb.net:27017/test?ssl=true&replicaSet=smartindia-shard-0&authSource=admin&retryWrites=true")
app.secret_key = 'mysecret'
db = client.Gaming.users

# ######## ---- AI agent functions start ---- ########


def setup_initial():
    """ Initial Setup of parameters """
    global levels_per_game
    global maximum_state
    global curr_state

    get_levels()
    get_total_each()
    for indx, key in enumerate(maximum_state):
        curr_state[key] = 0


def get_total_each():
    """ Returns total score possible in each module """
    global levels_per_game
    global filename
    global maximum_state
    data = ET.parse(filename)
    root = data.getroot()
    for indx, game in enumerate(root):
        for param in game:
            for str_key in param.attrib:
                maximum_state[str_key] = maximum_state[str_key] + float(param.attrib[str_key])*levels_per_game[indx]


def get_levels():
    global levels_per_game
    data = ET.parse(filename)
    root = data.getroot()
    levels_per_game = []
    for game in root:
        levels_per_game.append(int(game.attrib['levels']))


def find_heuristic(game_id, level):

    # get game_state
    global filename
    global curr_state
    global curr_score
    global maximum_state
    _, game_state = get_info_game(game_id, level)

    # assume perfect score acheived no matter what game is played [under-estimate of path]
    for key in game_state:
        curr_state[key] = curr_state[key] + game_state[key]
        curr_score[key] = curr_score[key] + game_state[key]

    # find max_score (% wise ) in which intelligence type, min_state (%) amongst all [ minimum in terms of games played ]
    score_percentages = {}
    state_percentages = {}
    for key in curr_score:
        if curr_state[key] == 0:
            score_percentages[key] = 0
        else:
            score_percentages[key] = curr_score[key]/curr_state[key]
        state_percentages[key] = curr_state[key]/maximum_state[key]
    # get the intelligence type with the highest percentage
    max_key = max(score_percentages, key=score_percentages.get)
    min_key = min(state_percentages, key=state_percentages.get)
    # get the dist from upper threshold amd that curr/max of that intelligence type
    heur_val2 = thld_one - state_percentages[max_key]
    heur_val1 = thld_common - state_percentages[min_key]

    # no use going for this
    if game_state[min_key] == 0:
        return beta*heur_val2

    if heur_val1 > 0 and heur_val2 > 0:
        return alpha*heur_val1 + beta*heur_val2
    elif heur_val2 < 0 and heur_val1 > 0:
        return alpha*heur_val1
    elif heur_val2 > 0 and heur_val1 < 0:
        return alpha*heur_val2


def goal_test():
    """ Return True if goal achieved, else false """
    global curr_state
    global maximum_state
    temp_dict = {}
    for key in curr_state:
        temp_dict[key] = curr_state[key]/maximum_state[key]
    score_check1 = [v > thld_one for v in temp_dict.values()]
    score_check2 = [v > thld_common for v in temp_dict.values()]
    # minimum requirement of each state not met
    if False in score_check2:
        return False
    # all requirements fulfilled
    if True in score_check1:
        return True
    # no clear maximum
    return False


def find_games_left():
    """ returns the actual game id """
    global levels_per_game
    global levels_done

    games_left_id = []
    for indx, val in enumerate(levels_per_game):
        if val - levels_done[indx] > 0:
            games_left_id.append(indx + 1)  # game id is 1 + indx
    return games_left_id


def get_info_game(idx, level):
    global filename
    data = ET.parse(filename)
    root = data.getroot()
    game_state = {}
    for game in root:
        if game.attrib['ID'] == str(idx):
            mod_name = game.attrib['module_name' + str(level)]
            for param in game:
                for key in param.attrib:
                    game_state[key] = float(param.attrib[key])
    print(game_state)
    return mod_name, game_state

# ######## ---- AI agent functions ends ---- ########


def getLog():
    login = session.get('logged_in', '')
    if login:
        return 'yes'
    else:
        return 'no'


def ai(score_variable):
    global initial_state
    global maximum_state
    global levels_per_game
    global levels_done
    global games_played
    global curr_state
    global curr_score

    if games_played < 8:
        # # choose a game randomly
        game_choice_id = random.choice(range(1, games_limit))
        if levels_done[game_choice_id - 1] == 0:
            # # get the score and the updated state after playing the game
            module_name, game_state = get_info_game(game_choice_id, 1)
            # # score is the actual score
            for key in curr_state:
                curr_score[key] = curr_score[key] + game_state[key]*score_variable
                curr_state[key] = curr_state[key] + game_state[key]

            # update call_game function, it needs to simply return the module_name.
            games_played = games_played + 1
            # increment to show the level at which a player is
            levels_done[game_choice_id - 1] = 1
            return module_name
    else:
        if goal_test():
            return "game_ended"
        games_left_id = find_games_left()
        game_choice_id = 0
        max_heur_score = 0

        for game_id in games_left_id:
            temp_heur_score = find_heuristic(game_id, levels_done[game_id - 1] + 1)
            if temp_heur_score > max_heur_score:
                max_heur_score = temp_heur_score
                game_choice_id = game_id
        # -1 since the index is 1 less than actual id
        module_name, game_state = get_info_game(game_choice_id,  levels_done[game_choice_id - 1] + 1)

        for key in curr_state:
            curr_score[key] = curr_score[key] + game_state[key]*score_variable
            curr_state[key] = curr_state[key] + game_state[key]

        games_played = games_played + 1
        # increment to show the level at which a player is
        levels_done[game_choice_id - 1] = levels_done[game_choice_id - 1] + 1
        return module_name


@app.route('/call', methods=['GET', 'POST'])
def call():
    pprint("Session Score: " + str(session['finalscore']))
    game = callai()
    pprint("Game Selected by AI: " + str(game))
    return render_template('Screens.html', game=game)


def callai():
    game = ai(float(session['finalscore']))
    return game


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')


@app.route('/loginaction', methods=['POST', 'GET'])
def login():
    lvalue = 'no'
    number = int(request.form['username'])
    login_user = db.find_one({'Username': number})
    if login_user:
        if bcrypt.hashpw(request.form['pwd'].encode('utf-8'), login_user['Password']) == login_user['Password']:
            pprint(session['sid'])
            session['logged_in'] = True
            session['username'] = number
            lvalue = 'yes'
            return render_template('home.html', l=lvalue, name=login_user['First Name'])
        else:
            return "Error"
    else:
        return "Error"


@app.route('/firstpage', methods=['GET', 'POST'])
def firstpage():
    return render_template('start.html')


@app.route('/fungames', methods=['GET', 'POST'])
def fungames():
    lvalue = getLog()
    return render_template('fungames.html', l=lvalue)


@app.route('/testgame', methods=['GET', 'POST'])
def testgame():
    lvalue = getLog()
    return render_template('testgame.html', l=lvalue)


@app.route('/startgame', methods=['GET', 'POST'])
def startgame():
    lvalue = getLog()
    global initial_state
    global maximum_state
    global levels_per_game
    global levels_done
    global games_played
    global curr_state
    global curr_score

    setup_initial()
    levels_done = [0 for i in levels_per_game]
    games_played = 0
    curr_score = {}
    for key in curr_state:
        curr_score[key] = 0
    game = ai(0)
    print("FirstGame: " + game)

    return render_template('FirstScreen.html', game=game, l=lvalue)


@app.route('/register', methods=['GET', 'POST'])
def register():
    lvalue = getLog()
    return render_template('register.html', l=lvalue)


@app.route('/registeraction', methods=['GET', 'POST'])
def registeraction():
    lvalue = getLog()
    existing_user = db.find_one({'Username': request.form['phn']})
    if existing_user is None:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        usrn = request.form.get('usrn')
        pwd = request.form.get('pwd')
        rpwd = request.form.get('rpwd')
        if pwd == rpwd:
            hashpass = bcrypt.hashpw(request.form['pwd'].encode('utf-8'), bcrypt.gensalt())
        else:
            return "Passwords don't match!"
        db.insert({
            "Username": int(usrn),
            "First Name": fname,
            "Last Name": lname,
            "Email": email,
            "Password": hashpass
        })
        return redirect(url_for('home'))


@app.route('/bulls', methods=['GET', 'POST'])
def bulls():
    import CowBull
    level = int(request.form.get('level'))
    finalscore = CowBull.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint("Bulls:" + str(finalscore))
    return "1"


@app.route('/natureexplore', methods=['GET', 'POST'])
def natureexplore():
    import farmgame
    farmgame.start_game()
    # level = int(request.form.get('level'))
    finalscore = natureexplore.start_game()
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


@app.route('/slidingpuzzle', methods=['GET', 'POST'])
def slidingpuzzle():

    level = int(request.form.get('level'))
    filepath = './pictures'
    if level == 1:
        import slidingpuzzle_1.py
        finalscore = slidingpuzzle_1.start_game(filepath)
    elif level == 2:
        import slidingpuzzle_2.py
        finalscore = slidingpuzzle_2.start_game(filepath)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


@app.route('/memorymusic', methods=['GET', 'POST'])
def memorymusic():
    import memoryMusic
    level = int(request.form.get('level'))
    finalscore = memoryMusic.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint(str(finalscore))
    return "1"


@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    import hangman
    level = int(request.form.get('level'))
    finalscore = hangman.mainloop(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    pprint("Hangman:" + str(finalscore))
    return "1"


@app.route('/isometric1', methods=['GET', 'POST'])
def isometric1():
    return render_template('indexN1.html')


@app.route('/isometricscore', methods=['GET', 'POST'])
def isometricscore():
    sc = request.form.get('score')
    print("Score: " + str(sc))
    session['finalscore'] = sc
    return "1"


@app.route('/isometric2', methods=['GET', 'POST'])
def isometric2():
    return render_template('indexN2.html')


@app.route('/getout1', methods=['GET', 'POST'])
def getout1():
    return render_template('indexG.html')


@app.route('/getoutscore', methods=['GET', 'POST'])
def getoutscore():
    sc = request.form.get('score')
    print("Score: " + str(sc))
    session['finalscore'] = sc
    return redirect(url_for('call'))


@app.route('/connect4', methods=['GET', 'POST'])
def connect4():
    import connect4
    finalscore = 0
    level = int(request.form.get('level'))
    connect4.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Connect4: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


@app.route('/spacewars', methods=['GET', 'POST'])
def spacewars():
    import spacewars1
    finalscore = 0
    level = int(request.form.get('level'))
    spacewars1.start_game()
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("Spacewars: " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


@app.route('/natureqna', methods=['GET', 'POST'])
def natureqna():
    import nature
    finalscore = 0
    level = int(request.form.get('level'))
    nature.start_game(level)
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    pprint("NatureQNA" + str(level) + ": " + str(finalscore))
    session['finalscore'] = finalscore
    return "1"


@app.route('/animalsound', methods=['GET', 'POST'])
def animalsound():
    import music1
    music1.start_game()
    print("In animalsound")
    finalscore = 0
    f = open("score.txt", "r")
    s = f.read()
    finalscore = float(s.strip())
    session['finalscore'] = finalscore
    return "1"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)