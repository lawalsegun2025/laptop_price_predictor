import streamlit as st
import pandas as pd 
import numpy as np 
import pickle 

file1 =  open("pipeline.pkl", "rb")
rf = pickle.load(file1)
file1.close()

# Apple,Ultrabook,8,Mac,1.37,0,1,226.98300468106115,Intel Core i5,0,128,Intel

data = pd.read_csv("cleaned_X_train_data.csv")

data["IPS"].unique()

st.title("Laptop Price Predictor")

company = st.selectbox("Brand", data["Company"].unique())
