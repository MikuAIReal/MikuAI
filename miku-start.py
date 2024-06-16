import requests
import time
import json


global ques
global headers
global mikuoutput

ques = {'model': "bringusai/miku"}
headers = {"Content-Type": "application/json"}
WIDTH = 640
HEIGHT = 480


def ask():
    imput = input("input here mr. tester man: ")
    ques['prompt'] = imput
    #ques['format'] = "json"
    ques['stream'] = False

    mikuattack = json.dumps(ques)

    mikuattack2 = json.loads(mikuattack)

    global x
    
    x = requests.post("http://127.0.0.1:11434/api/generate", json = mikuattack2, headers = headers)


print("MikuAI reqiures Ollama please install it or have a heart attack")

time.sleep(2)

ask()

time.sleep(2)
mikuoutput = x.text["response"]

print(mikuoutput)
