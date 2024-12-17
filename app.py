import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Carregando o modelo treinado
with open('modelo/modelo_treinado.pkl', 'rb') as f:
    model = pickle.load(f)

# Definindo um modelo Pydantic para os dados de entrada
class InputData(BaseModel):
    cement: float
    slag: float
    flyash: float
    water: float
    superplasticizer: float
    coarseaggregate: float
    fineaggregate: float
    age: float

@app.get('/')
def home():
    return "Hello World"

@app.post('/predict')
def predict(input_data: List[InputData]):
    # Convertendo os dados recebidos para um DataFrame
    df_input = pd.DataFrame([item.dict() for item in input_data])
    
    # Fazendo as previsões
    y_pred = model.predict(df_input)
    
    # Retornando as previsões
    predictions = [{"prediction": pred} for pred in y_pred]
    return {"predictions": predictions}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host = "0.0.0.0", port = 8000, reload = True)
