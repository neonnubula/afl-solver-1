from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Index page accessed")  # Debug print
    if request.method == 'POST':
        # Extract data from form
        input_name = request.form.get('player_name')
        input_di = float(request.form.get('disposal_line'))
        input_gls = float(request.form.get('goal_line'))
        input_loc = request.form.get('location')
        input_opp = request.form.get('opposition')
        input_ven = request.form.get('venue')
        input_ssns = int(request.form.get('season'))
        input_time = request.form.get('time')
        input_day = request.form.get('day_of_week')

        # Read the CSV data into a DataFrame
        df = pd.read_csv('test-data.csv')
        
        # Here you would include the analysis functions and calculations
        # (Code for analysis goes here)
        
        # Instead of a temporary response, pass the results to a template
        # return render_template('results.html', ...)
        
        # Temporary response for debugging
        return "Form submitted successfully"
    else:
        # Render the form template
        return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)

