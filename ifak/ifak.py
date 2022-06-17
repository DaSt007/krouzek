from operator import length_hint
from random import randint
from time import sleep
from turtle import width
import pyglet
from data.data2 import states
from pyglet import image
from pprint import pprint

x = 1280
y = 720

window = pyglet.window.Window(x, y)

window.set_caption("-------------------------------------------------------------------------------------------------------------Ifak-------------------------------------------------------------------------------------------------------------")

state = '1'
final_state = '3'

image1 = pyglet.resource.image('background.jpg')
image2 = pyglet.resource.image('cave.png')
image3 = pyglet.resource.image('death.jpg')

icon1 = pyglet.image.load('16_16.png')
icon2 = pyglet.image.load('32_32_2.jpg')
window.set_icon(icon1, icon2)

label = pyglet.text.Label('',
                          font_name='Times New Roman'
                          ,
                          font_size=10,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

label2 = pyglet.text.Label(states[state].get('description', ''),
                          font_name='Times New Roman',
                          font_size=10,
                          x=window.width//2, y=window.height//2 + 50,
                          anchor_x='center', anchor_y='center',)



@window.event
def on_text(text):
    
    global states
    global state
    global final_state

    label.text += text
    

    targetstate = states[state].get('options', {}).get(text)

    print(targetstate)
    if targetstate:
        state = targetstate['target']
        label2.text = targetstate.get('description', '')


        # obsahuje boj
        fight = states[state].get('fight')
        if fight and not fight.get('passed'):
            label.text = fight.get('intro', '')
            label2.text = ''
            fight_result = False
            on_draw()
            print("boj des")
            sleep(2)

            player = randint(0, 10)
            oponent = randint(0, 5)
            label2.text = f"Tvoje sila je {player}, nepritele sila je {oponent}"
            on_draw()
            sleep(2)
            if player >= oponent:
                fight_result = True
                label.text = fight.get('win', '')
            else:
                label.text = fight.get('lost', '')

            if fight_result:
                fight['passed'] = True
            else:
                state = final_state
                return
        print(state)

        label.text = states[state].get('description', '')
        # on_draw()
            



@window.event
def on_draw():
    window.clear()
    if state < '3':
        image1.blit(0,0)
    if state > '3':
        image2.blit(0,0)
    if state == '3':
        image3.blit(x/2, y/2)
    label.draw()
    label2.draw()


pyglet.app.run()