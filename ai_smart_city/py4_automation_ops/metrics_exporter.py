# Metrics Exporter
import random

def export_metrics():
    """
    Simulate system metrics export.
    """
    metrics = {
        "model_latency_ms": random.randint(80, 150),
        "requests_per_minute": random.randint(50, 200),
        "drift_detected": random.choice([True, False])
    }
    print("[📊 Metrics Exported]", metrics)
    return metrics
