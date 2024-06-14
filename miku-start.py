import requests
import time
import json
import genshin
engine = genshin.Genshin()
engine.set_voice('miku_en')

def ask():
    input = input("input here mr. tester man: ")
    ques['prompt'] = input
    #ques['format'] = "json"
    ques['stream'] = False

    mikuattack = json.dumps(ques)

    global x
    
    x = requests.post("http://127.0.0.1:11434/api/generate", json = mikuattack, headers = headers)



papi = "http://127.0.0.1:11434/api/pull"
api = "http://127.0.0.1:11434/api/generate"
pull = { "name": "bringusai/miku" }
ques = {'model': "bringusai/miku"}
headers = {"Content-Type": "application/json"}



print("MikuAI reqiures Ollama please install it or have a heart attack")

time.sleep(2)

ask()


x1 = json.loads(x)

print(x.text)
print(x)
time.sleep(2)
mikuoutput = x.text["response"]

index = mikuoutput.find('s')
if index == -1:
    print("Not found.")
else:
    time.sleep(index / 10)
    mikuemo = happy



