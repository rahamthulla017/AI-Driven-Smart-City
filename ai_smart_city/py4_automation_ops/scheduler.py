# Job Scheduler
import time
from model_health_check import check_model_health
from drift_detection import detect_drift
from retraining_trigger import trigger_retraining
from metrics_exporter import export_metrics
import random

def automation_loop():
    old_mean = 50  # baseline
    while True:
        print("\n[🕒 Automation Cycle Running...]")
        health_ok = check_model_health()
        new_data = [random.randint(40, 60) for _ in range(10)]

        drift = detect_drift(new_data, old_mean)
        export_metrics()

        if not health_ok or drift:
            trigger_retraining()

        time.sleep(10)

if __name__ == "__main__":
    automation_loop()
