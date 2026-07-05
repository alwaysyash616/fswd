"""
Assignment: 28
Problem: 05
Topic: list and str mixed
Description: Write a Python script to count strings which ends at character 's' in a list of strings.
Date: 04-07-2026
"""

l1=['MySirG','VeoLMS','OpenAI','GCP','ChatGPT','YouTUBE','ChatGPT','MySirG']
count=0
for e in l1:
    if e.endswith('s'):
        count+=1
print(count)