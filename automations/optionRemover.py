import re

# Specify the path to your HTML file
file_path = 'automations/dataList_corrected.html'

# Read the content of the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Use regular expression to find all option tags and remove the display text
updated_content = re.sub(r'<option value="([^"]+)">[^<]*</option>', r'<option value="\1" </option>', content)

# Write the modified content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("The datalist options have been updated.")