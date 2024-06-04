import requests
import time
import json

papi = "http://127.0.0.1:11434/api/pull"
api = "http://127.0.0.1:11434/api/generate"
pull = { "name": "bringusai/miku" }
ques = {'model': "bringusai/miku"}



print("MikuAI reqiures Ollama please install it or have a heart attack")

time.sleep(2)

requests.post(papi, json = pull)

input = input("input here mr. tester man: ")

ques['prompt'] = input
ques['format'] = "json"
ques['stream'] = False

mikuattack = json.dumps(ques)

x = requests.post(api, json = mikuattack)



