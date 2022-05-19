import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write("# Classificação de Cancer")
st.write("## Breast Cancer Wisconsin (Diagnostic)")

st.sidebar.write("### Parâmetros")
xtreino, xteste, ytreino, yteste, df , classes= return_data(dataset) 
st.dataframe(df.sample(n = 5 , random_state = 1)) 
st.subheader("Classes") 
for idx, value in enumerate (classes): 
    st.text('{}: {}'.format(idx , value))
    
    



with open("objetos.pkl", "rb") as arquivo:
  ss, dtc = pickle.load(arquivo)

  #estrutura = {'perimeter': perimeter, 'area': area, 'compactness': compactness, 'concavity': concavity}
  #df = pd.DataFrame(estrutura, index=[0])
  
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
