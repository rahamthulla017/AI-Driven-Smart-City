# py3_model_serving/model_registry.py

def load_model(name: str):
    """
    Simulated model loader for AI Smart City project.
    In production, this would load a trained model from disk, S3, or SageMaker.
    """

    # Simulate different model behaviors based on name
    def anomaly_detector(features):
        return {"prediction": "normal", "confidence": 0.93}

    def traffic_forecast(features):
        return {"prediction": "high_traffic", "confidence": 0.88}

    # Register available mock models
    registry = {
        "anomaly_detector_v1": anomaly_detector,
        "traffic_forecast_v1": traffic_forecast,
    }

    # Return requested model or fallback to default
    model = registry.get(name)
    if not model:
        raise ValueError(f"Model '{name}' not found in registry.")

    return model
