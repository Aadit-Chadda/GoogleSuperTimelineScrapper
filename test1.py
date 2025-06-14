import pandas as pd
import json

with open('output.json', 'r') as file:
    comments = json.load(file)

df = pd.DataFrame(comments)
df.to_csv('analysis_output.csv', index=False, encoding='utf-8')
print("successfully converted .JSON file to .CSV")
