IDLE = 0
WASHING = 1
PAUSED = 2
DOOROPEN = 3
DONE = 4
OFF = 5

button_A_pressed = False
button_B_pressed = False
knob_pressed = False
starting_time = control.millis()
currentState = IDLE
currentTime = 0

def Volume():
    pass

def Spin():
    pass

def WashingLiquid():
    pass



def playSound():
    for i in range(4):
        music.playTone(Note.C, music.beat(BeatFraction.Whole))

def on_button_pressed_a():
    global button_A_pressed
    button_A_pressed = True
    pass

def on_button_pressed_b():
    global button_B_pressed
    button_B_pressed = True
    pass

def knob_pressed():
    global knob_pressed
    knob_pressed = True
    pass

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def updateSystem():
    global starting_time
    global currentTime
    global button_A_pressed
    global button_B_pressed
    
    if(currentState == IDLE):
        start_time_ms = control.millis()
        if(button_B_pressed):
            currentTime = #stop
        if (button_A_pressed):
            currentTime = 0
    if(currentState == WASHING):
        current_time_ms = control.millis()
        if(current_time_ms - start_time_ms) > 1000:
            currentTime -= 1
            start_time_ms = current_time_ms


def get_knob_data():
    analogValue = pins.analog_read_pin(AnalogPin.P1)
    return Math.map(analogValue, 0, 1023, 0, 270)

def LightWash():


def 

def HeavyWash():
    

def updateSystem():
    button_A_pressed
    button_B_pressed
    knob_pressed
    currentTime
    starting_time
    