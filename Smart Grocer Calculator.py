import streamlit as st

st.title("Smart Grocer Calculator")

st.write("**Enter Required Quantity**")

Rice_quantity = st.number_input("Rice Quantity (\u20B960/kg): ",step=0.5)
Sugar_quantity = st.number_input("Sugar Quantity (\u20B945/kg): ",step=0.5)
Oil_quantity = st.number_input("Oil Quantity (\u20B9120/kg): ",step=0.5)

Price_rice= 60
Price_sugar = 45
Price_oil= 120

total=0
discount=0
Final_Amount=0
if st.button("Calculate Bill"):
    total=(Rice_quantity*Price_rice)+(Sugar_quantity*Price_sugar)+(Oil_quantity*Price_oil)

    discount=0
    if total>500:
       discount= total*0.10

    Final_Amount=total-discount

st.divider()

st.subheader("**Bill Summary**")
st.write(f"**Purchase**:  {total:.2f}")
st.write(f"**Discount**:  {discount:.2f}")
st.write(f"**Total Amount**:  {Final_Amount:.2f}")








    
    