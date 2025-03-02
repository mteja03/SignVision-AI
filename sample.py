import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('/Users/atharvaamolthoke/Desktop/Sign-Language-Detection-Website-main/Trained_model.h5')

# Print the TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

# Print the Keras version
print(f"Keras version: {tf.keras.__version__}")