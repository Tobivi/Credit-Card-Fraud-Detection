import streamlit as st
import pandas as pd
import numpy as np
import pickle
import scikit-learn

pickle_in = open('creditcardfraud.pkl', 'rb')
model = pickle.load(pickle_in)

st.title("Credit Card Fraud Detection App")


st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.
**This app is built in order to detect fraudulent credit card transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**        
""")


st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("""Input Sender ID""")
receiver_name = st.sidebar.text_input("""Input Receiver ID""")
step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
types = st.sidebar.subheader(f"""
                 Enter Type of Transfer Made:\n\n\n\n
                 0 for 'Cash In' Transaction\n 
                 1 for 'Cash Out' Transaction\n 
                 2 for 'Debit' Transaction\n
                 3 for 'Payment' Transaction\n  
                 4 for 'Transfer' Transaction\n""")
types = st.sidebar.selectbox("",(0,1,2,3,4))
x = ''
if types == 0:
    x = 'Cash in'
if types == 1:
    x = 'Cash Out'
if types == 2:
    x = 'Debit'
if types == 3:
    x = 'Payment'
if types == 4:
    x =  'Transfer'
    
amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("""Original Balance Before Transaction was made""",min_value=0, max_value=110000)
newbalanceorg= st.sidebar.number_input("""New Balance After Transaction was made""",min_value=0, max_value=110000)
oldbalancedest= st.sidebar.number_input("""Old Balance""",min_value=0, max_value=110000)
newbalancedest= st.sidebar.number_input("""New Balance""",min_value=0, max_value=110000)
isflaggedfraud = 0
if amount >= 200000:
  isflaggedfraud = 1
else:
  isflaggedfraud = 0


if st.button("Detection Result"):
    values = {
    "step": step,
    "types": types,
    "amount": amount,
    "oldbalanceorig": oldbalanceorg,
    "newbalanceorig": newbalanceorg,
    "oldbalancedest": oldbalancedest,
    "newbalancedest": newbalancedest,
    "isflaggedfraud": isflaggedfraud
    }


    st.write(f"""### These are the transaction details:\n
    Sender ID: {sender_name}
    Receiver ID: {receiver_name}
    1. Number of Hours it took to complete: {step}\n
    2. Type of Transaction: {x}\n
    3. Anount Sent: {amount}\n
    4. Previous Balance Before Transaction: {oldbalanceorg}\n
    5. New Balance After Transaction: {newbalanceorg}\n
    6. Old Balance Destination Recepient Balance: {oldbalancedest}\n
    7. New Balance Destination Recepient Balance: {newbalancedest}\n
    8. System Flag Fraud Status: {isflaggedfraud}
                """)
    
    if sender_name=='' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is not fraudulent .""")
        
        
    st.write("Developed by: Oduyebo oluwatobi victor")
