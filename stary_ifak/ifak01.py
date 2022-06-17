from time import sleep
from random import randint
from data import states

print("Vitej dobrodruhu")

state = "7"

while True :

    if not states[state].get("fight", {}).get("passed", True):
        print(states[state]["fight"]["intro"])
        sleep(1)
        if 50 > randint(0,100):
            print(states[state]["fight"]["death"])
            state = "3"
            continue

        states[state]["fight"]["passed"] = True
        print(states[state]["fight"]["outtro"])

    print(states[state]["description"])
    i = input(": ")
    

    while i not in states[state]["options"] and i != "x":
        print("Napsal jsi neco jineho, zkus to znovu")
        i = input(": ")

    if i == "x":
        exit()
    

    print(states[state]["options"][i]["description"])
    state = states[state]["options"][i]["target"]
   
