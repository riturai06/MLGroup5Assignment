import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import sklearn

app=Flask(__name__,template_folder='templates')
model = pickle.load(open('Group5_Trained_MultiNB_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11',
       'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21',
       'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount' ]
    
    data = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(data)
        
    if output == 1:
        res_val = " Fraud Transaction!!!**"
    else:
        res_val = " Genuine Transaction "
        

    return render_template('index.html', prediction_text='This Transaction is {}'.format(res_val))

if __name__ == "__main__":
    app.run()