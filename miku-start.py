import requests
import time
import json

papi = "http://127.0.0.1:11434/api/pull"
api = "http://127.0.0.1:11434/api/generate"
pull = { "name": "bringusai/miku" }
ques = {'model': "bringusai/miku"}
headers = {"Content-Type": "application/json"}



print("MikuAI reqiures Ollama please install it or have a heart attack")

time.sleep(2)



#y = requests.post(papi, json = pull)

#print(y)

input = input("input here mr. tester man: ")

ques['prompt'] = input
#ques['format'] = "json"
#ques['stream'] = false

mikuattack = json.dumps(ques)

print(mikuattack)

#mikuattack3 = {"model": "bringusai/miku", "prompt": "hi", "stream": False}


mikuattack2 = json.loads(mikuattack)

print(type(mikuattack2))

x = requests.post("http://127.0.0.1:11434/api/generate", json = mikuattack2, headers = headers)

print(x.text)
print(x)




