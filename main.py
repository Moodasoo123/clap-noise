def on_sound_loud():
    music.play_melody("G A G E F A B C5 ", 130)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_sound_quiet():
    music.play_melody("- - - - - - - - ", 120)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)
