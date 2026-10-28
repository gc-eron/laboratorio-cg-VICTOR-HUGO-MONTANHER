import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Padrão Psicodélico / Geométrico")

k = st.slider("k", 1, 50, 10)
y, x = np.indices((128, 128))

def padrao(x, y, k):
    cx, cy = x - 64, y - 64
    
    dist = np.sqrt(cx**2 + cy**2)
    angulo = np.arctan2(cy, cx)
    
    ondas = np.sin(dist / (k + 1) * np.pi) * 127 + 127
    espiral = np.cos(angulo * k + dist / 10) * 127 + 127
    
    resultado = (ondas + espiral) / 2
    return resultado

imagem = padrao(x, y, k).astype(np.uint8)
st.image(ampliar(imagem, 4), caption="Padrão Gerado Dinamicamente")