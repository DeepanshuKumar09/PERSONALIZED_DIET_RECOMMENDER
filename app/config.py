from pathlib import Path

BASE_DIR = Path(__file__).parent

CSS_PATH = BASE_DIR / "Personalized_Diet_Recommendation/style.css"
IMAGE_PATH = BASE_DIR / "Personalized_Diet_Recommendation/images" / "Personalized_Diet_Recommendation/images/pat.png"

MODEL_PATH = BASE_DIR / "Personalized_Diet_Recommendation/assets" / "Personalized_Diet_Recommendation/assets/wellness_model (2).h5"
SCALER_X_PATH = BASE_DIR / "Personalized_Diet_Recommendation/assets" / "Personalized_Diet_Recommendation/assets/scaler_X.pkl"
SCALER_Y_PATH = BASE_DIR / "Personalized_Diet_Recommendation/assets" / "Personalized_Diet_Recommendation/assets/scaler_y.pkl"
FEATURES_PATH = BASE_DIR / "Personalized_Diet_Recommendation/assets" / "Personalized_Diet_Recommendation/assets/feature_cols.json"

GEMINI_API_KEY = "ENTER_YOUR_API_KEY"
