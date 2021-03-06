import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write("# Classificação de Cancer")
st.write("## Breast Cancer Wisconsin (Diagnostic)")

st.sidebar.write("### Parâmetros")
st.sidebar.slider("Perimeter", 40.0, 190.0, 100.0)
st.sidebar.slider("Area", 184.0, 4254.0, 881.0)
st.sidebar.slider("Compactness", 0.01, 1.6, 0.25)
st.sidebar.slider("Concavity", 0.0, 1.30, 0.27)
    

with open("objetos.pkl", "rb") as arquivo:
  ss, dtc = pickle.load(arquivo)

  estrutura = {'perimeter': perimeter, 'area': area, 'compactness': compactness, 'concavity': concavity}
  df = pd.DataFrame(estrutura, index=[0])
  
  st.write("### Parâmetros de Entrada")
  st.write(df)
  
  df = ss.transform(df)
  st.write(df)
  
  predicao = dtc.predict(df)
  st.write(f"A classe é: **{predicao[0]}**")
  
  predicao = dtc.predict_proba(df)
  predicao = pd.DataFrame(predicao)
  predicao.rename({
     'M' : 0,
     'B' : 1
  }, axis=1, inplace=True)
  
  st.write("Probabilidades")
  st.write(predicao)

