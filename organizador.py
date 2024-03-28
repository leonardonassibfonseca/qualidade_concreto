import pickle
import pandas                                  as pd
import numpy                                   as np

class Projeto:
    def __init__(self):
        self.home_path = 'transformacoes/'
        self.age_mms = pickle.load(open(self.home_path + 'transformacoes_age_mms.pkl', 'rb'))
        self.cement_mms = pickle.load(open(self.home_path + 'transformacoes_cement_mms.pkl', 'rb'))
        self.coarseaggregate_mms = pickle.load(open(self.home_path + 'transformacoes_coarseaggregate_mms.pkl', 'rb'))
        self.fineaggregate_mms = pickle.load(open(self.home_path + 'transformacoes_fineaggregate_mms.pkl', 'rb'))
        self.flyash_mms = pickle.load(open(self.home_path + 'transformacoes_flyash_mms.pkl', 'rb'))
        self.slag_mms = pickle.load(open(self.home_path + 'transformacoes_slag_mms.pkl', 'rb'))
        self.superplasticizer_mms = pickle.load(open(self.home_path + 'transformacoes_superplasticizer_mms.pkl', 'rb'))
        self.water_mms = pickle.load(open(self.home_path + 'transformacoes_water_mms.pkl', 'rb'))

    def transformacao_dos_dados(self, df5):
        df5['age'] = self.age_mms.transform(df5[['age']].values)
        df5['cement'] = self.cement_mms.transform(df5[['cement']].values)
        df5['coarseaggregate'] = self.coarseaggregate_mms.transform(df5[['coarseaggregate']].values)
        df5['fineaggregate'] = self.fineaggregate_mms.transform(df5[['fineaggregate']].values)
        df5['flyash'] = self.flyash_mms.transform(df5[['flyash']].values)
        df5['slag'] = self.slag_mms.transform(df5[['slag']].values)
        df5['superplasticizer'] = self.superplasticizer_mms.transform(df5[['superplasticizer']].values)
        df5['water'] = self.water_mms.transform(df5[['water']].values)

    #def get_prediction(self, modelo, dados_original, dados_teste):
    #    pred = modelo.predict(dados_teste)
    #    dados_original['Score'] = pred[:, 1].tolist()
    #    return dados_original.to_json(orient = 'records', date_format = 'iso')

    def get_prediction(self, modelo, dados_original, dados_teste):
        # Transformar os dados de teste antes de fazer a previsão
        self.transformacao_dos_dados(dados_teste)
    
        # Fazer a previsão com o modelo
        pred = modelo.predict(dados_teste)
    
        # Adicionar as previsões aos dados originais
        dados_original['Score'] = pred.tolist()
    
        # Retornar os resultados em formato JSON
        return dados_original.to_json(orient = 'records', date_format = 'iso')
