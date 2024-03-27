import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding

def get_max(moves, labels):
    moves = [[1 if move == 1 else 2 for move in sequence] for sequence in moves]

    max_length = 10 
    moves_padded = tf.keras.preprocessing.sequence.pad_sequences(
        moves, maxlen=max_length, padding='post', truncating='post')
    
    model = Sequential([
        Embedding(input_dim=3, output_dim=64, input_length=max_length),
        LSTM(128, return_sequences=True, dropout=0.2), 
        LSTM(64, dropout=0.2),  
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])
    
    model.fit(moves_padded, labels, epochs=10, batch_size=32)

    predictions = model.predict(moves_padded)
    max_index = np.argmax(predictions)
    max_moves = moves_padded[max_index]
    max_p = predictions[max_index]

    return max_moves, max_p