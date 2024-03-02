from bs4 import BeautifulSoup

# Step 1: Read dataList.html content
with open('dataList.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find the `player_names` datalist
datalist = soup.find('datalist', id='player_names')

# Step 4 & 5: Iterate through <option> tags and set the player names as its text
for option in datalist.find_all('option'):
    player_name = option['value']
    # Optional: You might want to strip the team name if it follows a consistent format
    player_name_only = ' '.join(player_name.split(' ')[:-1])
    option.string = player_name_only

# Step 6: Save the modified content back (this example overwrites the original file)
with open('dataList_corrected.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

# Notice: This code overwrites the original dataset with the correct format.
# Ensure to have a backup if needed or adjust the code to save to a new file.