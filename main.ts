input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.stopMelody(MelodyStopOptions.All)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.InBackground)
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    music.changeTempoBy(20)
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    music.changeTempoBy(-20)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.stopMelody(MelodyStopOptions.All)
    music.play(music.stringPlayable("A B F E D G D D ", 318), music.PlaybackMode.InBackground)
})
