from flask import Flask, render_template, request
from solver import solver

# Import solver from the solver.py file


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        input_name = request.form.get('player_name')
        input_di = float(request.form.get('disposal_line'))
        input_gls = float(request.form.get('goal_line'))
        input_loc = request.form.get('location')
        input_opp = request.form.get('opposition')
        input_ven = request.form.get('venue')
        input_ssns = int(request.form.get('season'))

        # Process data
        gamesHit, totals, percentages = solver(input_name, input_di, input_gls, input_loc, input_opp, input_ven, input_ssns)
        summary = prep_summary(gamesHit, totals, percentages, input_name, input_di, input_gls, input_loc, input_opp, input_ven)

        # Return results template with summary
        return render_template('results.html', summary=summary)

    # Show input form by default
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')



# dictionary within dictionary style?

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Process form submission...

#         gamesHit, totals, percentages = solver(input_name, input_di, input_gls, input_loc, input_opp, input_ven, input_ssns)

#         # Prepare the data dictionary
#         data = {
#             'gamesHit': gamesHit, 
#             'totals': totals, 
#             'percentages': percentages,
#             'input_name': input_name,
#             'input_di': input_di,
#             'input_gls': input_gls,
#             'input_loc': input_loc,
#             'input_opp': input_opp,
#             'input_ven': input_ven,
#             'input_ssns': input_ssns
#         }

#         summary = generate_summary(data)
#         return render_template('results.html', summary=summary)

#     return render_template('index.html')
