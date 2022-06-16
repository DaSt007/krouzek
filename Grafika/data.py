states = {
    "1": {
        "name": "vstup do hry",
        "description": "Vitej dobrosruhu, pokud chces zacit sve dobrodruzstvi <0>, pokud ne <1>",
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
        "name": "zacatecni mistnost",
        "description": "Jeskyne tady pokracuje tremi smery, na sever <s> a na jih <j> a na vychod <v>",
        "options": {
            "s": {
                "target": "5",
                "description": 'Jdes na sever az do chvile, kdy narazis na mistnost s truhlou'
            },
            "j": {
                "target": "7",
                "description": "Jdes na jih az do chvile, kdy narazis na mmistnost s tlacitkem"
            },
            "v": {
                "target": "6",
                "description": "Jdes na jih az do chvile, kdy narazis na prazdnou mmistnost"
            },
        }
    },
    "5": {
        "name": "mistnost s truhlu 01",
        "description": "V teto mistnosti muzes otevrit truhlu <0>, nebo pokracovat na vychod <v>, nebo jit na jihovychod <jv>, nebo jit na jih <j>",
        "options": {
            "0": {
                "target": "3",
                "description": "Otevrel jsi truhlu a pod tebou se otevrela past do ktere jsi spadl. UMREL JSI"
            },
            "v": {
                "target": "8",
                "description": ""
            },
            "jv": {
                "target": "6",
                "description": "Jdes na jiovychod do prazdne mistnosti"
            },
            "j": {
                "target": "4",
                "description": "Vratil ses do mistnosti ve ktere ses poprve objevil"
            },
        }
    },
    "6": {
        "name": "mistnost 01",
        "description": "Tato mistnost pokracuje tremi smery, na zapad <z>, na vychod <v> a na severozapad <sz>",
        "options": {
            "z": {
                "target": "4",
                "description": "Vratil ses do mistnosti ve ktere ses poprve objevil"
            },
            "v": {
                "target": "3",
                "description": "Zvuky se stale priblizuji, ale ty se porat nehybes. Najednou jsou zvuky hned vedle tebe a ty si uvedomis ze je to skreti banda. Uz je pozde na to utect. Skreti te sezerou za ziva"
            },
            "sz": {
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
                "description": "Chvili prozkoumavas toto podivuhodne misto, kdyz najednou te spatri skret se kterym zacnes bojovat"
            },
        }
    },
    "8": {
        "name": "boj se skretem",
        "fight": {
            "passed": False,
            "intro": "V tomto boji si pomerite vase sily",
            "win": "Brutalne jsi zavrazdil skreta a muzes pokracovat",
            "lost": "Roztrhal te na kusy a pak tvoje kosti pouzil jako zachod",
                    },
        "description": "Jsi v chodbe, muzes jit na zapad 'z'",
        "options": {
            "z": {
                "target": "7",
                "description": "Jde se ti dobre"
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
