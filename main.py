import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit Hello Worldiiii gweb')

st.write("interactive widgets")

text = st.text_input("あなたの趣味は？")
"あなたの趣味は", text, "です。"

condition = st.sidebar.slider("今の調子は？", 0, 100, 50)
"コンディション", condition


img = Image.open(r"C:\Users\arai3\tech0\LPBS\images\gwen.jpg")
st.image(img,caption="gwen", use_container_width=True)
