# Iris Prediction API

A machine learning API built with Python, FastAPI and scikit-learn.
It takes 4 flower measurements and predicts the species.

## Run it

pip install -r requirements.txt
uvicorn app:app --reload

## Try it

http://127.0.0.1:8000/predict?sl=5.1&sw=3.5&pl=1.4&pw=0.2

Returns: {"species": "setosa"}