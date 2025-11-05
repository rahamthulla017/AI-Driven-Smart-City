# 🚀 Script to post multiple sensor events from CSV to FastAPI ingestion API
import requests, csv, json, time, os

# API endpoint (make sure the FastAPI ingestion service is running)
url = "http://localhost:8001/ingest"

# Get the absolute path to the CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "samples", "sensor_sample.csv")

# Read CSV and post each row as JSON
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        payload = {
            "sensor_id": row['sensor_id'],
            "timestamp": row['timestamp'],
            "metric": row['metric'],
            "value": float(row['value']),
            "metadata": {}
        }

        try:
            resp = requests.post(url, json=payload, timeout=5)
            print(f"✅ Sent: {payload} → Status {resp.status_code}")
            print("Response:", resp.json())
        except Exception as e:
            print("❌ Failed to send:", e)
        
        time.sleep(0.3)  # small delay between requests
