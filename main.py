def on_button_pressed_a():
    music.stop_melody(MelodyStopOptions.ALL)
    music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_right():
    music.change_tempo_by(20)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    music.change_tempo_by(-20)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    music.stop_melody(MelodyStopOptions.ALL)
    music.play(music.string_playable("A B F E D G D D ", 318),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)
