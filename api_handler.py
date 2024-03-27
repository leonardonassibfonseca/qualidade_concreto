import pickle
import pandas as pd
from flask import Flask, request, Response

from organizador import Projeto

# Carregar as credenciais
#credentials, project_id = google.auth.default()

# Criar um cliente com as credenciais
#client = storage.Client(credentials=credentials, project=project_id)
    
# Acesso ao bucket onde o modelo treinado está armazenado
#bucket_name = 'armazenamento-qualidade-concreto'
#bucket = client.get_bucket(bucket_name)

# Carregar modelo treinado
#blob_path_modelo = 'modelo/modelo_treinado.pkl'
#blob_modelo = bucket.blob(blob_path_modelo)
#blob_modelo.download_to_filename('/tmp/modelo_treinado.pkl')

# Carregar o modelo treinado usando pickle
#modelo = pickle.load(open('/tmp/modelo_treinado.pkl', 'rb'))
modelo = pickle.load(open('/modelo/modelo_treinado.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    teste_json = request.get_json() #Recebe um arquivo JSON a partir da request

    if teste_json:  #Se o teste_json for diferente de vazio, ou seja, se foi carregado algum dado
        #Verifica se o arquivo passado é um tipo de dicionário e se sim, foi enviado um arquivo com somente uma linha
        if isinstance(teste_json, dict):
            #Cria um dataframe e para isso é necessário indicar no Pandas qual é o nº da linha inicial, nesta caso, 0
            dados_que_vieram_da_producao = pd.DataFrame(teste_json, index=[0])
        else:
            #Se não for é um dicionário, foi enviado um arquivo com mais de uma linha
            dados_que_vieram_da_producao = pd.DataFrame(teste_json, columns = teste_json[0].keys())

        #Instanciando a classe do projeto, neste caso, HealthInsurance
        pipeline = Projeto()

        #Transformação dos dados
        df5 = pipeline.transformacao_dos_dados(dados_que_vieram_da_producao)

        #predição
        df_resposta = pipeline.get_prediction(modelo, dados_que_vieram_da_producao, df5)
        
        return df_resposta
    else:
        return Response('{}', status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    #Dizer para endpoint rodar no localhost (rodando na máquina)
    #port = os.environ.get('PORT', 5000)
    #app.run('0.0.0.0', port = port)
    #app.run('0.0.0.0')
    app.run(host='0.0.0.0', port = 5000)
#172.25.114.131 -> endereço IPv4 pc local
#app.run('0.0.0.0')
