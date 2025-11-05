# Feature Engineering Entry Point
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(title="Feature Engineering Service")

# Incoming data model
class SensorEvent(BaseModel):
    sensor_id: str
    timestamp: str
    metric: str
    value: float
    metadata: dict

@app.get("/")
def home():
    return {"message": "Feature Engineering API is running successfully."}

@app.post("/features")
def extract_features(event: SensorEvent):
    # Simulate some feature computations
    avg_value = round(event.value * random.uniform(0.8, 1.2), 2)
    anomaly_score = abs(event.value - avg_value)
    count = random.randint(10, 50)

    return {
        "sensor_id": event.sensor_id,
        "metric": event.metric,
        "avg_value": avg_value,
        "count": count,
        "anomaly_score": anomaly_score,
        "timestamp": event.timestamp
    }

@app.get("/health")
def health():
    return {"status":"running"}