import mne
import numpy as np

# Function to load raw EEG data
def load_eeg_data(file_path):
    """Loads EEG data from a file."""
    raw = mne.io.read_raw_edf(file_path, preload=True)
    print(f"Data loaded from {file_path}")
    return raw

# Function to filter EEG data
def filter_data(raw_data, low_freq=1, high_freq=50):
    """Applies bandpass filter to EEG data."""
    raw_data.filter(low_freq, high_freq, fir_design='firwin')
    print(f"Data filtered between {low_freq}Hz and {high_freq}Hz")
    return raw_data
