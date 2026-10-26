import streamlit as st
from photo import load_bw_photo, new_photo
from metrics import calculate

st.title("Simulación Foto Sin Luz :)")

file = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

if file is None:
    st.info("Sube una imagen para comenzar D:")
    st.stop()

threshold = st.slider("Umbral", min_value = 70, max_value = 170, value = 128)
height = st.number_input("Altura", min_value = 32, max_value = 1300, value = 200)
width = st.number_input("Ancho", min_value = 32, max_value = 1300, value = 200) 
invert = st.checkbox ("Invertir")

matrix = load_bw_photo(file, height, width, threshold, invert)
new = new_photo(matrix)

col1, col2, col3 = st.columns(3)
with col1:
    st.caption("Original")
    st.image(file)
with col2:
    st.caption("Blanco y negro")
    st.image(matrix)
with col3: 
    st.caption("Cuantica")
    st.image(new)

bombs, bombs_detected, percentage = calculate(matrix, new)

st.metric("Bombas", round(bombs))
st.metric("Bombas detectadas", round(bombs_detected))
st.metric("Porcentaje final", round(percentage, 5))

