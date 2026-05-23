from music21 import converter, instrument, note, chord
import glob
notes = []
for file in glob.glob("dataset/*.mid"):
    print("Processing:", file)
    midi = converter.parse(file)
    parts = instrument.partitionByInstrument(midi)
    if parts:
        notes_to_parse = parts.parts[0].recurse()
    else:
        notes_to_parse = midi.flat.notes
    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(
                str(element.pitch)
            )
        elif isinstance(element, chord.Chord):
            notes.append(
                '.'.join(
                    str(n)
                    for n in element.normalOrder
                )
            )
print("Total Notes:", len(notes))
sequence_length = 4
pitchnames = sorted(set(notes))
note_to_int = dict(
    (note, number)
    for number, note
    in enumerate(pitchnames)
)
network_input = []
network_output = []
for i in range(
    0,
    len(notes) - sequence_length
):
    sequence_in = notes[
        i:i + sequence_length
    ]
    sequence_out = notes[
        i + sequence_length
    ]
    network_input.append(
        [
            note_to_int[n]
            for n in sequence_in
        ]
    )
    network_output.append(
        note_to_int[sequence_out]
    )
print("Total Sequences:",
      len(network_input))
import numpy as np
n_patterns = len(network_input)
network_input = np.reshape(
    network_input,
    (
        n_patterns,
        sequence_length,
        1
    )
)
network_input = network_input / float(
    len(pitchnames)
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
model = Sequential()
model.add(
    LSTM(
        128,
        input_shape=(
            network_input.shape[1],
            network_input.shape[2]
        )
    )
)
model.add(Dropout(0.2))
model.add(Dense(64))
model.add(Dense(
    len(pitchnames),
    activation='softmax'
))
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam'
)
model.summary()
model.fit(
    network_input,
    np.array(network_output),
    epochs=50,
    batch_size=16
)
model.save(
    "model/music_model.h5"
)
print("Model Saved!")