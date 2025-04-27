import matplotlib.pyplot as plt
import mne

# Plot the EEG data
def plot_eeg_data(raw_data):
    """Plots the EEG signal."""
    raw_data.plot(duration=5, n_channels=30, scalings='auto')

# Save processed data
def save_data(raw_data, output_path):
    """Saves processed EEG data."""
    raw_data.save(output_path, overwrite=True)
    print(f"Data saved to {output_path}")
