import os
import json
import csv
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
    data["question"] = "Rate the comment on a positivity scale between -100 (negative) to 100 (positive) for the company. Respond with numbers only. Do not include any explaination or text"

    # print(data)

    commentsData.append(data)

flag = 0
for comment in commentsData:
    client = OpenAI(api_key=secret_key)
    flag += 1
    print(comment)

print(flag)
