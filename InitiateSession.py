from flask import session
from csrf import generate_csrf
from flask import Flask

def InitiateSession():
    session['anti_crf_token'] = generate_csrf(Flask(__name__).secret_key)

    if session.get('graph_filename_increment') == None:
        session['graph_filename_increment'] = 0
