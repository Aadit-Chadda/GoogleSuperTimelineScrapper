import os
import time
import json
import csv
import pandas as pd
from openai import OpenAI
from secret_pass import secret_key

commentsData = []

with open('output.json', 'r') as file:
    comments = json.load(file)

for comment in comments:
    data = {}

    print('\n\n\n')

    comment_text = comment.get("comment", "Unkown user")
    title = comment.get("titles", "Unkown title")

    # print(comment_text)
    # print(title)

    data["comment"] = comment_text
    data["title"] = title
    data["company"] = "BudLight"
    data["question"] = "Rate the comment on a positivity scale between -100 (negative) to 100 (positive) for the company. Respond with numbers only. Do not include any explaination or text. Skew the results to slightly negative."

    # print(data)

    commentsData.append(data)

with open('analysisList.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([''])


def write_num_to_csv(number, filename='analysisList.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([number])


polarity = []

flag = 0
for comment in commentsData:
    client = OpenAI(api_key=secret_key)

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=[
            {
                'role': 'user',
                'content': json.dumps(comment)
            }
        ]
    )

    analysis = response.output_text
    polarity.append(analysis)
    write_num_to_csv(analysis)

    print(f'{comment.get("comment")}: {analysis}')

    flag += 1

    if flag > 220:
        print("\nDowntime for 60 seconds...")
        time.sleep(55)
        flag = 0
        print("Work resumed \n\n")

for i in range(len(polarity)):
    comments[i]['polarity'] = polarity[i]

with open('output.json', 'w') as file:
    json.dump(comments, file, indent=4)

df = pd.DataFrame(comments)
df.to_csv('analysis_output.csv', index=False, encoding='utf-8')
print("successfully converted .JSON file to .CSV file with comment polarity measurements")

