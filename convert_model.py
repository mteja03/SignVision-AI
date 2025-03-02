import tensorflow as tf
from tensorflow import keras
import h5py
import json

# Define your model architecture (Modify if needed)
def build_model():
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D(2, 2),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(26, activation='softmax')  # Assuming 26 classes (A-Z)
    ])
    return model

# Rebuild the model
new_model = build_model()

# Load weights from the old .h5 file
h5_model_path = "Trained_model.h5"
new_model.load_weights(h5_model_path)

# Save the model in the new .keras format
new_model.save("Trained_model_new.keras", save_format="keras")

print("✅ Model successfully converted to 'Trained_model_new.keras'.")
