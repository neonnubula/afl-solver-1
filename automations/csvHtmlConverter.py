import csv

def csv_to_html_datalist(csv_filename):
    with open(csv_filename, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        player_list = list(reader)
    
    if not player_list:
        print("The CSV file is empty.")
        return

    # Use the first player as the datalist id
    datalist_id = player_list[0][0]
    
    # Start HTML datalist construction
    html_output = f'<datalist id="{datalist_id}">\n'
    
    # Add the remaining players as options
    for player in player_list[1:]:  # Excludes the first since it's used as the id
        # Updated to ensure option tags are correctly opened and closed
        html_output += f'    <option value="{player[0]}"></option>\n'
    
    html_output += '</datalist>'
    
    # Output the final HTML
    print(html_output)
  
csv_to_html_datalist('playerList2023.csv')