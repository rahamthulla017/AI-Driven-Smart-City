from fastapi import FastAPI
import httpx

app = FastAPI(title="AI Smart City API Gateway", version="1.0")

# URLs of your Python microservices
SERVICE_URLS = {
    "ingestion": "http://127.0.0.1:8001/health",
    "feature_engineering": "http://127.0.0.1:8002/health",
    "model_serving": "http://127.0.0.1:8003/health"
}

@app.get("/")
def home():
    return {"message": "🚀 AI Smart City API Gateway is running", "docs": "/docs"}

@app.get("/aggregate")
async def aggregate_services():
    results = {}
    async with httpx.AsyncClient(timeout=5.0) as client:
        for name, url in SERVICE_URLS.items():
            try:
                resp = await client.get(url)
                results[name] = resp.json()
            except Exception as e:
                results[name] = {"status": "error", "details": str(e)}
    return {"gateway_status": "ok", "services": results}
