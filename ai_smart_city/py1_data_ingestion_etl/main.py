# FastAPI Ingestion API Entry Point
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os, csv, datetime

app = FastAPI(title="SmartCity - Data Ingestion (Python)")

DATA_DIR = os.path.join(os.getcwd(), "py1_data_ingestion_etl", "data")
os.makedirs(DATA_DIR, exist_ok=True)
SAMPLE_STORE = os.path.join(DATA_DIR, "smartcity_ingest.csv")

class SensorEvent(BaseModel):
    sensor_id: str
    timestamp: str
    metric: str
    value: float
    metadata: dict = {}

@app.get("/health")
def health():
    return {"status":"running"}

@app.post("/ingest")
def ingest(evt: SensorEvent):
    # validate timestamp
    try:
        _ = datetime.datetime.fromisoformat(evt.timestamp)
    except Exception:
        raise HTTPException(status_code=400, detail="timestamp must be ISO format")
    header = not os.path.exists(SAMPLE_STORE)
    with open(SAMPLE_STORE, "a", newline="") as out:
        writer = csv.writer(out)
        if header:
            writer.writerow(['sensor_id','timestamp','metric','value','metadata'])
        writer.writerow([evt.sensor_id, evt.timestamp, evt.metric, evt.value, evt.metadata])
    return {"status":"ok", "saved_to": SAMPLE_STORE}
