import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "ml" / "model.pkl"

class BurnoutModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

    def predict(self, features: dict) -> float:
        if self.model is None:
            return 0.0
        X = np.array([[features["engagement"], features["burnout"],
                       features["workload"], features["conflicts"]]])
        return float(self.model.predict_proba(X)[0, 1])

model = BurnoutModel()
