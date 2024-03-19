from flask import Flask, render_template, request, session
from solver import solver
from summary import generate_summary
from csrf import CSRFProtect, generate_csrf
from GetCSVOptionList import get_csv_option_list
import pandas as pd

csrf = CSRFProtect()
app = Flask(__name__)
app.secret_key = 'AfLsOlVeRsEcReTkEy'
csrf.init_app(app)

@app.route('/')
def home():
    session['anti_crf_token'] = generate_csrf(app.secret_key)
    return render_template('layout.html', player_list=get_csv_option_list('player-list.csv'), venue_list=get_csv_option_list('venue-list.csv'), team_list=get_csv_option_list('team-list.csv'))


@app.route('/analysisform', methods = ['POST'])
def analysisform():
    if request.form.get('csrf_token') == session['anti_crf_token']:
        session['anti_crf_token'] = generate_csrf(app.secret_key)
        return render_template('index.html', player_list=get_csv_option_list('player-list.csv'), venue_list=get_csv_option_list('venue-list.csv'), team_list=get_csv_option_list('team-list.csv'))
    else:
        return render_template('Error.html')

@app.route('/results', methods = ['POST'])
def results():
    if request.form.get('csrf_token') == session['anti_crf_token']:
        session['anti_crf_token'] = generate_csrf(app.secret_key)
        # Extract form data
        input_id = int(request.form.get('player_id'))
        input_name = request.form.get('player_name')
        input_di = float(request.form.get('disposal_line'))
        input_gls = float(request.form.get('goal_line'))
        input_loc = request.form.get('location')
        input_opp = request.form.get('opposition')
        input_opp_id = int(request.form.get('opposition_id'))
        input_ven = request.form.get('venue')
        input_venue_id = int(request.form.get('venue_id'))
        input_ssns = int(request.form.get('season'))

        # Process data
        gamesHit, totals, percentages = solver(input_id, input_di, input_gls, input_loc, input_opp_id, input_venue_id, input_ssns)
        summary = generate_summary(gamesHit, totals, percentages, input_name, input_di, input_gls, input_loc, input_opp, input_ven,input_ssns)

        # Return results template with summary
        return render_template('results.html', summary=summary)
    else:
        return render_template('Error.html')

@app.route('/error', methods = ['GET'])
def error():
    return render_template('Error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('ErrorPage.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
