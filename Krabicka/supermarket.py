from dtbox.colors import *
from dtbox.wsled import WSLed
from time import sleep

ws = WSLed(num=16)

def kolecko(colour):
    
    ws.color(colour, i = 1)
    ws.color(colour, i = 2)
    ws.color(colour, i = 4)
    ws.color(colour, i = 7)
    ws.color(colour, i = 8)
    ws.color(colour, i = 11)
    ws.color(colour, i = 13)
    ws.color(colour, i = 14)
    
    sleep(2)
    
    for f in range(16):
        ws.color(BLACK, i = f)
    
    
def krizek(colour):
    
    ws.color(colour, i = 0)
    ws.color(colour, i = 3)
    ws.color(colour, i = 5)
    ws.color(colour, i = 6)
    ws.color(colour, i = 9)
    ws.color(colour, i = 10)
    ws.color(colour, i = 12)
    ws.color(colour, i = 15)
    
    sleep(2)
    
    for f in range(16):
        ws.color(BLACK, i = f)
    
while True:
    krizek(colour = (10, 0, 0))
    kolecko(colour= (0, 0, 10))