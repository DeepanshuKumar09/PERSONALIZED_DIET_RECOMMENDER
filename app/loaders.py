import tensorflow as tf
import joblib
import json
import streamlit as st

from config import (
    MODEL_PATH,
    SCALER_X_PATH,
    SCALER_Y_PATH,
    FEATURES_PATH
)
@st.cache_resource
def load_resources():
    model = tf.keras.models.load_model(
        MODEL_PATH,
        compile=False
    )

    scaler_X = joblib.load(
        SCALER_X_PATH
    )

    scaler_y = joblib.load(
        SCALER_Y_PATH
    )

    with open(FEATURES_PATH, "r") as f:
        feature_cols = json.load(f)

    return (
        model,
        scaler_X,
        scaler_y,
        feature_cols
    )
