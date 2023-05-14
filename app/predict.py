from fastapi import FastAPI
from xgboost import XGBClassifier

app = FastAPI()

model = XGBClassifier()
model.load_model("xgboost_model.pkl")

@app.get("/predict")
def predict(team1: str, team2: str, runs1: int, runs2: int):
    data = {
        "team1": team1,
        "team1": team1,
        "runs1": runs1,
        "runs2": runs2,
    }
    df = pd.DataFrame(data)

    prediction = model.predict(df)

    return prediction

if __name__ = "__main__":
    app.run()
