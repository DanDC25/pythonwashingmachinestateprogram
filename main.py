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
        for i in range(4):
            music.playTone(Note.C, music.beat(BeatFraction.Whole))

        if soundPrinted == False:
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
    global button_B_pressed
    global button_A_pressed
    if currentState == IDLE:
        starting_time = control.millis()
        if(button_B_pressed):
            button_B_pressed = False
            return WASHING
        if (button_A_pressed):
            button_A_pressed = False
            currentTime = 0
            return OFF
    if currentState == WASHING:
        current_time_ms = control.millis()
        while(current_time_ms - start_time_ms) > 1000:
            current_time_ms -= 1
            start_time_ms = current_time_ms
            return DONE
        if (button_A_pressed):
            button_A_pressed = False
            return DONE
        if (button_B_pressed):
            button_B_pressed = False
            return PAUSED
    if currentState == PAUSED:
        if (button_A_pressed):
            button_A_pressed = False
            return DONE
        if (button_B_pressed):
            button_B_pressed = False
            return WASHING
    if currentState == DONE:
        if (button_A_pressed):
            button_A_pressed = False
            return IDLE
    if currentState == OFF:
        if (button_A_pressed):
            button_A_pressed = False
            return IDLE

    
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
        serial.write_line("Done")



    if (currentState == OFF):
        basic.clear_screen()



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