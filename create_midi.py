from midiutil import MIDIFile
music = MIDIFile(1)
track = 0
time = 0
music.addTrackName(track, time, "Sample Track")
music.addTempo(track, time, 120)
notes = [60, 62, 64, 65, 67, 69, 71, 72]
duration = 1
volume = 100
for i, pitch in enumerate(notes):
    music.addNote(
        track,
        channel=0,
        pitch=pitch,
        time=i,
        duration=duration,
        volume=volume
    )
with open(
    "dataset/simple_song.mid",
    "wb"
) as output_file:
    music.writeFile(output_file)
print("MIDI file created successfully!")