from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract the form data
        input_name = request.form['name']
        input_disposals = float(request.form['disposals'])
        input_goals = float(request.form['goals'])
        input_location = request.form['location']
        input_opposition = request.form['opposition']
        input_venue = request.form['venue']
        input_seasons = int(request.form['seasons'])
        input_time = request.form['time']
        input_dayofweek = request.form['dayofweek']

        # Here you would call the functions from main.py to process the data
        # and generate the output to return to the user

        return 'Processing form data...'
    else:
        # Render the form for the user to fill out
        return 'Displaying form...'

if __name__ == '__main__':
    app.run(debug=True)