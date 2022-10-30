let IDLE = 0
let WASHING = 1
let PAUSED = 2
let DOOROPEN = 3
let DONE = 4
let OFF = 5
let button_A_pressed = false
let button_B_pressed = false
let knob_pressed = false
let starting_time = control.millis()
let currentState = IDLE
let currentTime = 0
let statePrinted = false
let soundPrinted = false
let TurnDegree = 270.0
function Volume(int: number) {
    
}

function Spin(int: number) {
    
}

function Softener(int: number) {
    
}

function Detergent(int: number) {
    
}

function playSound() {
    let soundPrinted: boolean;
    if (soundPrinted == false) {
        for (let i = 0; i < 4; i++) {
            music.playTone(Note.C, music.beat(BeatFraction.Whole))
        }
        soundPrinted = true
    }
    
}

function MeasureTurnDegree(): number {
    let someDegree = get_knob_data()
    return someDegree
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    button_A_pressed = true
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    button_B_pressed = true
    
})
function updateSystem() {
    
    
    
    
    if (input.buttonIsPressed(Button.B)) {
        button_B_pressed = true
    }
    
}

function evaluateState(state: number): number {
    let start_time_ms: number;
    let currentTime: number;
    let current_time_ms: number;
    if (currentState == IDLE) {
        start_time_ms = control.millis()
        if (button_B_pressed) {
            return WASHING
        }
        
        if (button_A_pressed) {
            currentTime = 0
            return DONE
        }
        
    }
    
    if (currentState == WASHING) {
        current_time_ms = control.millis()
        if (current_time_ms - start_time_ms > 1000) {
            currentTime -= 1
            start_time_ms = current_time_ms
            return DONE
        }
        
        if (button_A_pressed) {
            return DONE
        }
        
    }
    
    return state
}

function reactToState(int: number) {
    if (currentState == WASHING) {
        if (TurnDegree > 135) {
            HeavyWash()
        } else {
            LightWash()
        }
        
        basic.showLeds(`
                # . # . #
                # . # . #
                # . # . #
                # . # . #
                . # . # .
        `)
        serial.writeLine("Washing")
    }
    
    if (currentState == IDLE) {
        basic.showLeds(`
                . . # . .
                # . # . #
                # . # . #
                # . . . #
                . # # # .
        `)
        serial.writeLine("Idle")
    }
    
    if (currentState == PAUSED) {
        basic.showLeds(`
                . # # # .
                . # . # .
                . # # # .
                . # . . .
                . # . . .
        `)
        serial.writeLine("Paused")
    }
    
    if (currentState == DONE) {
        basic.showLeds(`
            # # # . .
                # . . # .
                # . . # .
                # . . # .
                # # # . .
        `)
        playSound()
    }
    
}

function get_knob_data(): number {
    let analogValue = pins.analogReadPin(AnalogPin.P1)
    return Math.map(analogValue, 0, 1023, 0, 270)
}

function LightWash() {
    Volume(1000)
    Spin(400)
    Softener(5)
    Detergent(5)
    serial.writeLine("Water 1000militer")
    serial.writeLine("Detergent 5militer")
    serial.writeLine("Softener 5militer")
    serial.writeLine("400RPM")
}

function HeavyWash() {
    let statePrinted: boolean;
    Volume(2000)
    Spin(400)
    Softener(10)
    Detergent(10)
    if (statePrinted == false) {
        serial.writeLine("Water 2liters")
        serial.writeLine("Detergent 10militer")
        serial.writeLine("Softener 10militer")
        serial.writeLine("400RPM")
        statePrinted = true
    }
    
}

basic.forever(function on_forever() {
    
    updateSystem()
    currentState = evaluateState(currentState)
    reactToState(currentState)
})
