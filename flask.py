# possible format:

from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Render input form (using an HTML string here for simplicity).
    return '''
        <form action="/process" method="post">
            Name: <input type="text" name="name"><br>
            Disposals: <input type="text" name="disposals"><br>
            Goals: <input type="text" name="goals"><br>
            Location: <input type="text" name="location"><br>
            Opposition: <input type="text" name="opposition"><br>
            Venue: <input type="text" name="venue"><br>
            Seasons: <input type="text" name="seasons"><br>
            Time: <input type="text" name="time"><br>
            Day of Week: <input type="text" name="dayofweek"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/process', methods=['POST'])
def process():
    # Read the form data
    input_name = request.form['name']
    input_disposals = float(request.form['disposals'])
    # more form fields here...

    # Read the CSV data into a DataFrame
    df = pd.read_csv('test-data.csv')

    # Functions here (as defined before)
    def count_disposals(value, df):
        # body of count_disposals
        # make sure to pass df and use it instead of the global df
        pass

    # all other functions are similarly defined

    # processing and calling analysis functions
    disposals_less, disposals_greater = count_disposals(input_disposals, df)
    # call other functions and gather results...

    # Create a response with the results
    response = {
        'disposals_less': disposals_less,
        'disposals_greater': disposals_greater,
        # include other results here...
    }

    # Return the response, here as simple text for demonstration:
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
