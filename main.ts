let IDLE = 0
let WASHING = 1
let PAUSED = 2
let DOOROPEN = 3
let DONE = 4
let OFF = 5
let button_A_pressed = false
let button_B_pressed = false
let starting_time = control.millis()
let currentTime = 0
function playSound() {
    for (let i = 0; i < 4; i++) {
        music.playTone(Note.C, music.beat(BeatFraction.Whole))
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    let button_A_was_pressed = true
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    let button_B_was_pressed = true
    
})
