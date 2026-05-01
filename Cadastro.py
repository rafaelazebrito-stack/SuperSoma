import streamlit as st

st.set_page_config(page_title="SuperSoma", layout="centered")

st.title("🔢 SuperSoma")

st.write("Digite dois números e clique em **Somar**")

# Entrada dos números
numero1 = st.number_input("Primeiro número", step=1.0)
numero2 = st.number_input("Segundo número", step=1.0)

# Botão de soma
if st.button("Somar"):
    resultado = numero1 + numero2
    st.success(f"✅ Resultado: {resultado}")