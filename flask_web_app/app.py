from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Assumes you have an 'index.html' template with the form

@app.route('/process', methods=['POST'])
def process():
    input_name = request.form['name']
    input_disposals = float(request.form['disposals'])
    input_goals = float(request.form['goals'])
    input_location = request.form['location']
    input_opposition = request.form['opposition']
    input_venue = request.form['venue']
    input_seasons = int(request.form['seasons'])
    input_time = request.form['time']
    input_dayofweek = request.form['dayofweek']

  # Load the CSV data into a DataFrame
    df = pd.read_csv('test-data.csv')

      # During development, you might print to your Flask console to verify
      # Replace this eventually with logging or actual data handling for production
      print(df)
      print()
      # Here you would normally process the input using the dataframe.
      # For now, return a success message or render a template with context
      return render_template('success.html', name=input_name)

    # Here you would normally process the input and then return something
    return "Processing the inputs. This functionality needs to be implemented."

if __name__ == '__main__':
    app.run(debug=True)

