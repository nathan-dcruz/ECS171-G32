from flask import Flask, render_template, request
import pandas as pd
from werkzeug.utils import secure_filename
import pickle
from sklearn import preprocessing
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures

app = Flask(__name__)

@app.route('/')
def show_predict_stock_form():
    return render_template('predictorform.html')

@app.route('/predict', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
      model = pickle.load(open("Support-Vector-Machine", "rb"))
      Xlabels = ["radius_mean","texture_mean","smoothness_mean","compactness_mean",
                 "symmetry_mean","fractal_dimension_mean","radius_se","texture_se",
                 "smoothness_se","compactness_se",
                 "symmetry_se",
                 "radius_worst","texture_worst",
                 "smoothness_worst","compactness_worst",
                 "symmetry_worst"]
      # Xtest = [17.99,10.38,0.1184,0.2776,
      #          0.2419,0.07871,1.095,0.9053,
      #          0.006399,0.04904,
      #          0.03003,
      #          25.38,17.33,
      #          0.1622,0.6656,
      #          0.4601]
      f = request.files["file"]
      if f:
        filename = secure_filename(f.filename)
        f.save(filename)
        df = pd.read_csv(filename)
        print(df)
        # scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        # df_rescaled = scaler.fit_transform(df)
        # df = pd.DataFrame(data = df_rescaled, columns = df.columns)
        train_set = pd.read_csv("Train_set.csv")
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_X = scaler.fit( train_set )
        test_X = scaler.transform( df )
        Y = model.predict(test_X)
        if Y == 1:
          cancer_type = "Malignant"
        else:
          cancer_type = "Benign"
        print(Y)
      else:
        Xdict = {}
        for i in range(len(Xlabels)):
          currentValue = request.form[Xlabels[i]]
          Xdict[Xlabels[i]] = [currentValue]
        X = pd.DataFrame(data=Xdict)

        train_set = pd.read_csv("Train_set.csv")
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_X = scaler.fit( train_set )
        test_X = scaler.transform( X )
        Y = model.predict(test_X)
        print(Y)
        if Y == 1:
          cancer_type = "Malignant"
        else:
          cancer_type = "Benign"
      return render_template('resultsform.html', cancer_type=cancer_type)
    
app.run("localhost", "9999", debug=True)
