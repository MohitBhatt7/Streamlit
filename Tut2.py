import streamlit as st 

st.title("Order placing app.")

if st.button("Place Order"):
    st.success("Your order is being placed.")
    
order = st.checkbox("Add items")

if order:
    st.success("Added items.")
    

Order_Food = st.radio("Please pick for food section:- ", ["Veg-Momo", "Veg Chilli", "Veg plates"])