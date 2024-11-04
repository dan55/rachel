import streamlit as st

st.set_page_config(page_title="Rachel's happiness level")

x = st.slider("**Select a value. How happy is Rachel right now?**", value=51)

if x > 75:
    st.write("Rachel is very happy :smile:.")
elif x > 50:
    st.write("Rachel is moderately happy :slightly_smiling_face:.")
elif x > 25:
    st.write("Rachel is not so happy :disappointed:.")
else:
    st.write("Rachel is not at all happy :tired_face:.")
