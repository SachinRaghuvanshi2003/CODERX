import requests
import json

API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# input="Generate a python code to check whether number is armstrong or not"
# for i in range(2):
# 	output=query({"inputs":input})
# 	input=output[0]['generated_text']
# 	print(input)
# for key in output:
# 		 print(key['generated_text'])