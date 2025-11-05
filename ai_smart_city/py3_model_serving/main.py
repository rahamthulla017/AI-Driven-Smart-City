from fastapi import FastAPI, HTTPException
from inference_service import predict
from model_registry import load_model
from ab_testing import ab_test_models

app = FastAPI(title="Model Serving API", version="1.0")

@app.get("/")
def home():
    return {"message": "Model Serving API is running successfully"}

@app.post("/predict")
def model_predict(payload: dict):
    try:
        model = load_model("anomaly_detector_v1")
        result = predict(model, payload)
        return {"version": "v1", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ab-test")
def model_ab_test(payload: dict):
    """Compare local vs sagemaker models"""
    result = ab_test_models(payload)
    return result

@app.get("/health")
def health():
    return {"status":"running"}
