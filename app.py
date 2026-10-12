from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app =FastAPI()
data =load_iris()
model = RandomForestClassifier().fit(data.data, data.target)

@app.get("/predict")
def predict(sl:  float, sw: float, pl:float, pw: float):
    pred = model.predict([[sl,  sw, pl, pw]]) [0]
    return {"species": str(data.target_names[pred])}

    
