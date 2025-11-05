# Model Health Monitoring
import requests

def check_model_health():
    try:
        r = requests.get("http://localhost:8002/health", timeout=3)
        if r.status_code == 200:
            print("[✅ Model Health OK]")
            return True
        else:
            print("[⚠️ Model Health Warning]", r.status_code)
            return False
    except Exception as e:
        print("[❌ Model Health Error]", e)
        return False
