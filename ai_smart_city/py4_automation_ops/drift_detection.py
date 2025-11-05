# Data Drift Detection
import numpy as np

def detect_drift(new_data, old_mean, threshold=0.2):
    """
    Compare new data mean with old mean to detect drift.
    Returns True if drift detected.
    """
    new_mean = np.mean(new_data)
    drift = abs(new_mean - old_mean) / old_mean
    if drift > threshold:
        print(f"[⚠️ Drift Detected] Old Mean: {old_mean}, New Mean: {new_mean}")
        return True
    return False
