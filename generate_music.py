from tensorflow.keras.models import load_model
model = load_model(
    "model/music_model.h5"
)
print("Music AI Model Loaded!")
from music21 import note, stream
output_notes = []
generated_notes = [
    "C4",
    "D4",
    "E4",
    "G4",
    "A4"
]
for pattern in generated_notes:
    new_note = note.Note(pattern)
    output_notes.append(new_note)
midi_stream = stream.Stream(output_notes)
midi_stream.write(
    'midi',
    fp='generated_music/output.mid'
)
print("Generated music saved!")