import streamlit as st

st.write("# Classificação de Cancer")
st.write("## Breast Cancer Wisconsin (Diagnostic)")

st.sidebar.write("### Parâmetros")
st.sidebar.slider("Radios", 7.8, 36.0, 16.3, 0.1)
st.sidebar.slider("Texture", 11.0, 50.0, 26.0, 0.1)
st.sidebar.slider("Perimeter", 49.0, 251.0, 107.0, 0.1)
st.sidebar.slider("Area", 184.0, 4254.0, 881.0, 0.1)
st.sidebar.slider("Smoothness", 0.06, 0.22, 0.14, 0.1)
st.sidebar.slider("Compactness", 0.01, 1.6, 0.25, 0.1)
st.sidebar.slider("Concavity", 0.0, 1.30, 0.27, 0.1)
st.sidebar.slider("Concave", 0.0, 0.30, 0.11, 0.1)
st.sidebar.slider("Symmetry", 0.14, 0.66, 0.30, 0.1)
st.sidebar.slider("Fractal", 0.054, 0.20, 0.08, 0.1)
