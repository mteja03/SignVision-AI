import h5py

# Path to your .h5 model file
h5_model_path = "Trained_model.h5"  # Make sure this file is in the same directory as this script

# Open and inspect the .h5 file
with h5py.File(h5_model_path, "r") as f:
    print("✅ Keys in .h5 file:", list(f.keys()))
