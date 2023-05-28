from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__)

@app.route('/')
def show_predict_stock_form():
    return render_template('predictorform.html')
@app.route('/predict', methods=['POST'])

def results():
    form = request.form
    if request.method == 'POST':
      model = pickle.load(open("Logistic-Regression-Model", "rb"))
      Xlabels = ["radius_mean","texture_mean","smoothness_mean","compactness_mean",
                 "symmetry_mean","fractal_dimension_mean","radius_se","texture_se",
                 "smoothness_se","compactness_se",
                 "symmetry_se",
                 "radius_worst","texture_worst",
                 "smoothness_worst","compactness_worst",
                 "symmetry_worst"]
      Xtest = [17.99,10.38,0.1184,0.2776,
               0.2419,0.07871,1.095,0.9053,
               0.006399,0.04904,
               0.03003,
               25.38,17.33,
               0.1622,0.6656,
               0.4601]
      Xdict = {}
      for i in range(len(Xlabels)):
        Xdict[Xlabels[i]] = [Xtest[i]]
      X = pd.DataFrame(data=Xdict)
      Y = model.predict(X)
      if Y == 1:
        cancer_type = "Malignant"
      else:
        cancer_type = "Benign"

      return render_template('resultsform.html', cancer_type=cancer_type)
    
app.run("localhost", "9999", debug=True)
