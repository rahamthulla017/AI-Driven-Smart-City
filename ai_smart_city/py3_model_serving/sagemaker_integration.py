# py3_model_serving/sagemaker_integration.py
import random

def sagemaker_predict(payload: dict):
    """
    Mock function to simulate SageMaker endpoint inference.
    In real implementation, this would call a deployed SageMaker model using boto3.
    """
    # Generate simulated result
    prediction = random.choice(["normal", "anomaly"])
    confidence = round(random.uniform(0.75, 0.98), 2)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "source": "sagemaker_mock"
    }

