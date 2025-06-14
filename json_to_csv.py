# converting the output JSON file to CSV file, in case the converter does not run properly in commentAnalysis.py

# importing all required libraries
import pandas as pd
import json

# reading all the comments and data in the output.json file
with open('output.json', 'r') as file:
    comments = json.load(file)

# converting the json data to a pandas Data Frame
df = pd.DataFrame(comments)
df.to_csv('analysis_output.csv', index=False, encoding='utf-8')  # exporting the Data Frame to a CSV file
print("successfully converted .JSON file to .CSV")
