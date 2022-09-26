from dtbox.wsled import WSLed
from time import sleep
from time import sleep.ms

ws = WSLed(num=16)

colors = [
    (60, 30, 0),
    (60, 15, 0),
    (60, 0, 0),
    (45, 0, 60),
    (0, 0, 60),
    (0, 60, 60),
    (20, 50, 0),
    (0, 60, 0),
    
]

positions = [
    1,
    2,
    4,
    11,
    13,
    14,
    7,
    8,
]

while True:
    for i in range(8):
        x = i + 0
        if x >= 8:
            x = x - 8
        ws.color(colors[0], positions[x])
        
        x = i + 1
        if x >= 8:
            x = x - 8
        ws.color(colors[1], positions[x])
        
        x = i + 2
        if x >= 8:
            x = x - 8
        ws.color(colors[2], positions[x])
        
        x = i + 3
        if x >= 8:
            x = x - 8
        ws.color(colors[3], positions[x])
        
        x = i + 4
        if x >= 8:
            x = x - 8
        ws.color(colors[4], positions[x])
        
        x = i + 5
        if x >= 8:
            x = x - 8
        ws.color(colors[5], positions[x])
        
        x = i + 6
        if x >= 8:
            x = x - 8
        ws.color(colors[6], positions[x])
        
        x = i + 7
        if x >= 8:
            x = x - 8
        ws.color(colors[7], positions[x])
        
        sleep.ms(200)
        