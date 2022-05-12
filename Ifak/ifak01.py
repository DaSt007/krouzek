from time import sleep
from random import randint


states = {
    "1": {
        "name": "vstup do hry",
        "description": "Pokud chces zacit sve dobrodruzstvi <0>, pokud ne <1>",
        "options": {
            "0": {
                "target": "2",
                "description": ""
            },
            "1": {
                "target": "3",
                "description": ""
            },
        }
    },
    "2": {
        "name": "druhe potvrzeni",
        "description": "Jsi si jisty ze to zvladnes? Ano! <0> Ne <1>",
        "options": {
            "0": {
                "target": "4",
                "description": "Probudis se na zemi. Jsi velice zmateny, protoze vubec nevis jak ses sem dostal. Rozhlidnes se okolo a rychle si uvedomis ze nejsi ve svem pokoji, ale v jeskyni."
            },
            "1": {
                "target": "3",
                "description": ""
            },
        }
    },
    "3": {
        "name": "konec",
        "description": "Hra zkoncila <x> pro ukonceni <r> pro restart",
        "options": {
            "x": {
                "target": "",
                "description": ""
            },
            "r": {
                "target": "1",
                "description": "Restartuje se"
            },
        }
    },
    "4": {
        "name": "vstup",
        "description": "Na sever od tebe jeskyne pokracuje <s> na jih konci utesem <j>",
        "options": {
            "s": {
                "target": "5",
                "description": 'Jdes na sever do chvile, kdy narazis na "rozdvojku"'
            },
            "j": {
                "target": "3",
                "description": "Sel jsi k utesu, ale zakopl jsi a spadl do vecnych hlubin"
            },
        }
    },
    "5": {
        "name": "prvni rozdeleni jeskyne",
        "description": "Cesta dale pokracuje na vychod smerem dolu <v>, nebo na zapad smerem nahoru <z>, nebo zpatky <0>",
        "options": {
            "v": {
                "target": "6",
                "description": ""
            },
            "z": {
                "target": "5",
                "description": 'Zda se ti jako bys stale zatacel do leva, az do chvile kdy narazis na nejspis tu stejnou "rozdvojku"'
            },
            "0": {
                "target": "4",
                "description": "Vratil ses"
            }
        },
    },
    "6": {
        "name": "druhe rozdeleni jeskyne",
        "description": "Nejdes dlouho a uz zacnes slyset zvuky. Chces zvuky nasledovat <0>, nebo jen zustat stat na miste <1>, nebo jit zpatky <2>",
        "options": {
            "0": {
                "target": "7",
                "description": "Zvuky se stale priblizuji. Najednou spatris to, co dela ty zvuky. Je to obrovska skreti kovarna"
            },
            "1": {
                "target": "3",
                "description": "Zvuky se stale priblizuji, ale ty se porat nehybes. Najednou jsou zvuky hned vedle tebe a ty si uvedomis ze je to skreti banda. Uz je pozde na to utect. Skreti te sezerou za ziva"
            },
            "2": {
                "target": "5",
                "description": "Vratil ses"
            },
        }
    },
    "7": {
        "name": "skteri kovarna",
        "description": "Muzes se vratit zpatky <0>, nebo kovarnu prozkoumat <1>",
        "options": {
            "0": {
                "target": "6",
                "description": "Vratil ses"
            },
            "1": {
                "target": "8",
                "description": "Chvili prozkoumavas toto podivuhodne misto, kdyz najednou te spatri skret. Ze zeme rychle zvednes kovovou tyc. Chces se skretem zacit boj <b>, nebo zkusit utect <u>"
            },
        }
    },
    "8": {
        "name": "boj se skretem",
        "description": "",
        "fight": {
            "passed": False,
            "intro": "Hnusny skret te chce bacit",
            "outtro": "Mrvola skreta",
            "death": "Rozmlatil te",
                    },
        "options": {
            "z": {
                "target": "7",
                "description": ""
            },
        }
    },
    "9": {
        "name": "",
        "description": "nice",
        "options": {
            "": {
                "target": "",
                "description": ""
            },
            "": {
                "target": "",
                "description": ""
            },
        }
    },
    "10": {
        "name": "",
        "description": "",
        "options": {
            "": {
                "target": "",
                "description": ""
            },
            "": {
                "target": "",
                "description": ""
            },
        }
    },
}



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
   
