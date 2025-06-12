import os
import json
import csv
from openai import OpenAI

with open('output.json', 'r') as file:
    comments = json.load(file)

for comment in comments:
    data = {}
    comment_text = comment.get("comment", "Unkown user")
    title = comment.get("titles", "Unkown title")

    print(comment_text)
    print(title)

    print('\n\n\n')

    data["comment"] = comment_text
    data["title"] = title
    data["company"] = "BudLight"
    data["question"] = "Rate the comment on a positivity scale between -100 (negative) to 100 (positive) for the company. Respond with numbers only. Do not include any explaination or text"

    print(data)
