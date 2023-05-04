import datetime
import os

# Get the current date and time
now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d %H:%M:%S')

# Get the path to the current directory and the filename of the script
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.basename(__file__)

# Create the path to the text file in the same directory as the script
text_file_path = os.path.join(dir_path, 'date.txt')

# Write the date string to the text file
with open(text_file_path, 'a') as file:
    file.write(date_string+'\n')

# Print a confirmation message
print(f'The current date and time ({date_string}) have been saved to {text_file_path}')
