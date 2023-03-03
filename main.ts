input.onSound(DetectedSound.Loud, function () {
    music.playMelody("G A G E F A B C5 ", 130)
})
input.onSound(DetectedSound.Quiet, function () {
    music.playMelody("- - - - - - - - ", 120)
})
