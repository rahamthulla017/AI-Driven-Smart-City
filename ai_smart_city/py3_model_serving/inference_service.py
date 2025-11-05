# py3_model_serving/inference_service.py
import random

def predict(model, payload: dict):
    """
    Simulated model inference function for Smart City project.
    In real usage, this would call an ML model's predict() or transform() method.
    """
    # Extract features safely
    features = payload.get("features") or [payload.get("value", 0)]
    
    # Simulate prediction output
    result = {
        "prediction": random.choice(["normal", "anomaly"]),
        "score": round(random.uniform(0.1, 0.99), 3),
        "model_used": model
    }

    return {
        "sensor_id": payload.get("sensor_id", "unknown"),
        "metric": payload.get("metric", "undefined"),
        "value": payload.get("value", 0),
        **result
    }
