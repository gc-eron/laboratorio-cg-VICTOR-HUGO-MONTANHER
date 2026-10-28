import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

bandeira = np.zeros((6,9,3), dtype=np.uint8)

st.title("Imagem como matriz")

bandeira[:3, :] = (255, 205, 0)
bandeira[3:5, :] = (0, 48, 135)
bandeira[5:, :] = (200, 16, 46)

bandeira2 = np.zeros((8, 8, 3), dtype=np.uint8)

bandeira2[:] = (218, 41, 28)

cor_cruz = (255, 255, 255)

bandeira2[3:5, 1:7] = cor_cruz
bandeira2[1:7, 3:5] = cor_cruz

bandeira3 = np.zeros((6,9,3), dtype=np.uint8)

bandeira3[:, :3] = (255, 130, 0)
bandeira3[:, 3:6] = (255, 255, 255)
bandeira3[:, 6:] = (0, 154, 68)

st.text("Colômbia:")
st.image(ampliar(bandeira))

st.text("Suíça:")
st.image(ampliar(bandeira2))

st.text("Costa do Marfim:")
st.image(ampliar(bandeira3))