import pickle
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Carregando o modelo treinado
with open('modelo/modelo_treinado.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get('/')
def home():
    return "Hello World"

# Definindo um modelo Pydantic para os dados de entrada no POST
class InputData(BaseModel):
    cement: float
    slag: float
    flyash: float
    water: float
    superplasticizer: float
    coarseaggregate: float
    fineaggregate: float
    age: float

    class Config:
        schema_extra = {"example": {"cement": 0.0,
                                    "slag": 0.0,
                                    "flyash": 0.0,
                                    "water": 0.0,
                                    "superplasticizer": 0.0,
                                    "coarseaggregate": 0.0,
                                    "fineaggregate": 0.0,
                                    "age": 0.0}}

@app.get('/predict')
def predict(cement: float,
            slag: float,
            flyash: float,
            water: float,
            superplasticizer: float,
            coarseaggregate: float,
            fineaggregate: float,
            age: float):
    
    # Criando um DataFrame a partir dos parâmetros recebidos
    df_input = pd.DataFrame({'cement': [cement],
                             'slag': [slag],
                             'flyash': [flyash],
                             'water': [water],
                             'superplasticizer': [superplasticizer],
                             'coarseaggregate': [coarseaggregate],
                             'fineaggregate': [fineaggregate],
                             'age': [age]})

    # Fazendo as previsões
    y_pred = model.predict(df_input)
    return {"prediction": y_pred[0]}

@app.post('/predict')
def predict_post(cement: float,
                 slag: float,
                 flyash: float,
                 water: float,
                 superplasticizer: float,
                 coarseaggregate: float,
                 fineaggregate: float,
                 age: float):
    
    # Criando um DataFrame a partir dos parâmetros recebidos
    df_input = pd.DataFrame({'cement': [cement],
                             'slag': [slag],
                             'flyash': [flyash],
                             'water': [water],
                             'superplasticizer': [superplasticizer],
                             'coarseaggregate': [coarseaggregate],
                             'fineaggregate': [fineaggregate],
                             'age': [age]})

    # Fazendo as previsões
    y_pred = model.predict(df_input)
    return {"prediction": y_pred[0]}

if __name__ == "__main__":    
    uvicorn.run("app:app", host = "0.0.0.0", port = 8000, reload = True)
