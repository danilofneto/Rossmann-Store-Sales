import pickle
import pandas as pd
from flask import Flask,request,Response
from rossman.Rossman import Rossman

model = pickle.load(open('C:/Users/Cliente/repos/DataScience_em_producao/model/model_rossmann.pkl', 'rb'))

app = Flask(__name__)
@app.route('/rossman/predict',methods=['POST'])

def rossman_predict():
    test_json= request.get_json()
    
    if test_json:
        if isinstance(test_json,dict):#Se tem apenas uma json
            test_raw=pd.DataFrame(test_json,index=[0])
        else:#se sai varios json concatenados
            test_raw=pd.DataFrame(test_json,columns=test_json[0].keys())
            
        pipeline = Rossman()
        df1 = pipeline.data_cleaning( test_raw)
        df2 = pipeline.feature_engineering(df1)
        df3 = pipeline.data_preparation(df2)
        df_response = pipeline.get_prediction(model,test_raw,df3)

        return df_response
    
    else:
        return Response('{}', status=200,mimetype='application/json')

    
if __name__ == '__main__':
    app.run('0.0.0.0')