import pgzrun
import pygame
import requests
import time
import json


global papi
global api
global pull
global ques
global headers
global mikuoutput


papi = "http://127.0.0.1:11434/api/pull"
api = "http://127.0.0.1:11434/api/generate"
pull = { "name": "bringusai/miku" }
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


def draw():
    screen.fill((255, 255, 255))  # Fill the screen with white color
    screen.blit(miku.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center
    if mikuemo == "happy":
        screen.blit(mikuh.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center
        time.sleep(indexh / 10)
    elif mikuemo == "sad":
        screen.blit(mikus.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center
        time.sleep(indexs / 10)
    elif mikuemo == "music":
        screen.blit(mikum.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center
        time.sleep(indexm / 10)
    else:
        screen.blit(miku.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center

def update():
    pass  # Add any game logic or updates here


print("MikuAI reqiures Ollama please install it or have a heart attack")

time.sleep(2)

ask()

print(x.text)
print(x)
time.sleep(2)
mikuoutput = x.text["response"]

indexh = mikuoutput.find('s')
if indexh == -1:
    print("Not found.")
else:
    mikuemo = "happy"

indexs = mikuoutput.find('s')
if indexs == -1:
    print("Not found.")
else:
    mikuemo = "sad"

indexm = mikuoutput.find('s')
if indexm == -1:
    print("Not found.")
else:
    mikuemo = "music"


pgzrun.go()