# py3_model_serving/ab_testing.py
from inference_service import predict
from model_registry import load_model
from sagemaker_integration import sagemaker_predict

def ab_test_models(payload: dict):
    """
    Run A/B testing between local model and SageMaker model simulation.
    Compares predictions and confidence values.
    """

    try:
        # Load local model
        local_model = load_model("anomaly_detector_v1")
        local_result = predict(local_model, payload)

        # Get simulated SageMaker model prediction
        sagemaker_result = sagemaker_predict(payload)

        # Determine comparison outcome
        decision = (
            "match"
            if local_result["prediction"] == sagemaker_result["prediction"]
            else "mismatch"
        )

        return {
            "local_result": local_result,
            "sagemaker_result": sagemaker_result,
            "decision": decision
        }

    except Exception as e:
        return {
            "error": str(e),
            "local_result": None,
            "sagemaker_result": None,
            "decision": "error"
        }
