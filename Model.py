import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import pickle

data_v1 = pd.read_csv("Admission_Predict_Ver1.1.csv")
data_v0 = pd.read_csv("Admission_Predict.csv")
data = pd.concat([data_v1, data_v0])

data = data.drop_duplicates()

data = data.drop(columns = ["Serial No."])

data = data.rename(columns={"Chance of Admit ": "Chance of Admit"})

def get_training_data(df):

    X = df.drop(columns = ["University Rating", "Chance of Admit"])
    y = df["Chance of Admit"]
    
    return X, y

def train_model(university_rating):
   
    df = data[data["University Rating"] == university_rating]
    print(df.shape)
    
    X, y = get_training_data(df)
    
    regressor = LinearRegression()
    regressor.fit(X, y)
    
    metric = cross_val_score(regressor, X, y, cv = 5)
    
    return regressor, metric

university_ratings = data["University Rating"].unique()
university_recommendations = {}

for u in university_ratings:
    regressor, metric = train_model(u)
    university_recommendations["University ranking " + str(u)] = {'model': regressor, 'metric': metric}

test = data.sample(20)
test = test.drop(columns = ["Chance of Admit", "University Rating"])

pickle.dump(regressor, open("university_recommendations.pkl", "wb"))