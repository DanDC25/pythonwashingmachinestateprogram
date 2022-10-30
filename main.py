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

statePrinted = False

soundPrinted = False

TurnDegree = 270.0

def Volume(int: volume):
    pass

def Spin(int: spin):
    pass

def Softener(int: softener):
    pass

def Detergent(int: detergent):
    pass



def playSound():
    if soundPrinted == False:
        for i in range(4):
            music.playTone(Note.C, music.beat(BeatFraction.Whole))
        soundPrinted = True

def on_button_pressed_a():
    global button_A_pressed
    button_A_pressed = True
    pass

def on_button_pressed_b():
    global button_B_pressed
    button_B_pressed = True
    pass

def MeasureTurnDegree():
    someDegree = get_knob_data()
    return someDegree

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def updateSystem():
    global starting_time
    global currentTime
    global button_A_pressed
    global button_B_pressed

    if (input.button_is_pressed(Button.B)):
        button_B_pressed = True
    


def evaluateState(state: int):
    if currentState == IDLE:
        start_time_ms = control.millis()
        if(button_B_pressed):
            return WASHING
        if (button_A_pressed):
            currentTime = 0
            return DONE
    if(currentState == WASHING):
        current_time_ms = control.millis()
        if(current_time_ms - start_time_ms) > 1000:
            currentTime -= 1
            start_time_ms = current_time_ms
            return DONE
        if (button_A_pressed):
            return DONE
    return state



def reactToState(int: currentState):
    if(currentState == WASHING):
        if TurnDegree > 135:
            HeavyWash()
        else:
            LightWash()
        
        basic.show_leds("""
                # . # . #
                # . # . #
                # . # . #
                # . # . #
                . # . # .
        """)

        serial.write_line("Washing")




    if(currentState == IDLE): 
        basic.show_leds("""
                . . # . .
                # . # . #
                # . # . #
                # . . . #
                . # # # .
        """)
        serial.write_line("Idle")

    if(currentState == PAUSED):
        basic.show_leds("""
                . # # # .
                . # . # .
                . # # # .
                . # . . .
                . # . . .
        """)
        serial.write_line("Paused")

    if(currentState == DONE):
        basic.show_leds("""
            # # # . .
                # . . # .
                # . . # .
                # . . # .
                # # # . .
        """)
        playSound()



def get_knob_data():
    analogValue = pins.analog_read_pin(AnalogPin.P1)
    return Math.map(analogValue, 0, 1023, 0, 270)

def LightWash():
    Volume(1000)
    Spin(400)
    Softener(5)
    Detergent(5)
    serial.write_line("Water 1000militer")
    serial.write_line("Detergent 5militer")
    serial.write_line("Softener 5militer")
    serial.write_line("400RPM")





def HeavyWash():
    Volume(2000)
    Spin(400)
    Softener(10)
    Detergent(10)
    if statePrinted == False:
        serial.write_line("Water 2liters")
        serial.write_line("Detergent 10militer")
        serial.write_line("Softener 10militer")
        serial.write_line("400RPM")
        statePrinted = True





def on_forever():
    global currentState
    updateSystem()
    currentState = evaluateState(currentState)
    reactToState(currentState)


basic.forever(on_forever)