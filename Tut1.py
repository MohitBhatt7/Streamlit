import streamlit as st 

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to our first interactive app.")
st.write("Please choose your favrouite chai:-")

Chai = st.selectbox("Your favrouite chai:-", ["Masala chai", "Lemon tea", "Adrak chai", "Kesar chai", "Elaichi chai"])

st.write(f"You choose {Chai}. Thats the great choice sir.")