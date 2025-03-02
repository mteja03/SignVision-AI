import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Define model architecture (Update this based on your original model)
def build_model():
    model = keras.Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(26, activation='softmax')  # Assuming 26 classes (A-Z)
    ])
    return model

# Build a new model
new_model = build_model()

# Load the old weights
new_model.load_weights("Trained_model.h5")

# Save it in the new format
new_model.save("Trained_model_new.keras", save_format="keras")

print("✅ Model successfully rebuilt and converted to 'Trained_model_new.keras'.")
