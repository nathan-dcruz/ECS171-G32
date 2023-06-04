# ECS171-G32 - Tumor Classification
Repository for ECS 171 Group 32, Spring Quarter 2023. The goal of this project is to classify tumors as benign or malignant given the tumor's physical attributes. A more comprehensive report of the project is included [here.](ECS171_Paper.pdf)

There are 3 machine learning models stored in this repository. Our dataset is located in Cancer_Data.csv.

## How to use the Jupyter Notebooks
To train and test a model, open the Jupyter Notebook for the model type you are interested in and run all the cells in the notebook. This will start the entire training process for that model from scratch, including data import and cleaning, training, testing, and statistics collection. Refer to the output of the cells to see information such as Accuracy, MSE, the ROC Curve, and more. 

## How to use the Demo
- To run the demo, run `ECS171-G32/front-end/app.py`
- You may either input numbers into the text boxes manually or upload a file. 
- If you choose to upload a file, make sure it is a `.csv` with only 1 row in it. Here is [a sample.](demo.csv)

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
