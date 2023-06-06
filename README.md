# ECS171-G32 - Tumor Classification
Repository for ECS 171 Group 32, Spring Quarter 2023. The goal of this project is to classify tumors as benign or malignant given the tumor's physical attributes. A more comprehensive report of the project is included [here.](ECS171_Paper.pdf)

There are 3 machine learning models stored in this repository. Our dataset is located in Cancer_Data.csv.

## How to use the Jupyter Notebooks
To train and test a model, open the Jupyter Notebook for the model type you are interested in and run all the cells in the notebook. This will start the entire training process for that model from scratch, including data import and cleaning, training, testing, and statistics collection. Refer to the output of the cells to see information such as Accuracy, MSE, the ROC Curve, and more. 

## How to use the demo
### Required dependencies
Please check whether you have all required dependencies:
- flask
- numpy
- pandas
- sklearn
- pickle
- matplotlib
- seaborn
- imblearn

### Instructions
- Make sure you are in the [frontend](./front-end) directory.
- Run `app.py` by `py app.py` (on Windows) or `python app.py` (on Mac).
- If the server is successfully running, you will be able to access the frontend demo on [localhost:9999](http://localhost:9999) using web browser.
- Once you open the web page, you have 2 options:
### Uploading a file
This is the primary option, and if you use uploading a file, data input will be ignored. However, please follow the file format as [demo.csv](./demo.csv) with the exact same header following by only one data row.

### Inputting data manually
You can also generate the output by manually entering every attribute, but make sure there is no file currently uploaded.

## Relevant files per model type
### Logistic Regression 
- `G32-Logistic-Regression.ipynb`: Jupyter Notebook for Logistic Regression. 
- `Logistic-Regression-Model`: A saved instance of a previously trained model. 

### Feed Forward Neural Network 
- `NN.ipynb`: Jupyter Notebook for Neural Network.
- `NN-Model`: A saved instance of a previously trained model. 

### Support Vector Machine 
- `SVM-Model.ipynb`: Jupyter Notebook for Support Vector Machine 
- `Support-Vector-Machine`: A saved instance of a previously trained model.
