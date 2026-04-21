import streamlit as st
import pandas as pd
import pickle

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
st.sidebar.markdown("""
**Enter Type of Transfer Made:**

- 0 for 'Cash In' Transaction
- 1 for 'Cash Out' Transaction
- 2 for 'Debit' Transaction
- 3 for 'Payment' Transaction
- 4 for 'Transfer' Transaction
""")
types = st.sidebar.selectbox("Transaction Type", (0, 1, 2, 3, 4))
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
    
amount = st.sidebar.number_input("Amount in $", min_value=0, max_value=100_000_000)
oldbalanceorg = st.sidebar.number_input("Original Balance Before Transaction was made", min_value=0, max_value=100_000_000)
newbalanceorg = st.sidebar.number_input("New Balance After Transaction was made", min_value=0, max_value=100_000_000)
oldbalancedest = st.sidebar.number_input("Old Balance (Destination)", min_value=0, max_value=100_000_000)
newbalancedest = st.sidebar.number_input("New Balance (Destination)", min_value=0, max_value=100_000_000)
isflaggedfraud = 1 if amount >= 200000 else 0


if st.button("Detection Result"):
    if sender_name == '' or receiver_name == '':
        st.error("Please input Transaction ID or Names of Sender and Receiver!")
    else:
        features = pd.DataFrame(
            [[step, types, amount, oldbalanceorg, newbalanceorg, oldbalancedest, newbalancedest, isflaggedfraud]],
            columns=['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud'],
        )
        prediction = model.predict(features)[0]

        st.write(f"""### These are the transaction details:\n
        Sender ID: {sender_name}
        Receiver ID: {receiver_name}
        1. Number of Hours it took to complete: {step}\n
        2. Type of Transaction: {x}\n
        3. Amount Sent: {amount}\n
        4. Previous Balance Before Transaction: {oldbalanceorg}\n
        5. New Balance After Transaction: {newbalanceorg}\n
        6. Old Destination Recipient Balance: {oldbalancedest}\n
        7. New Destination Recipient Balance: {newbalancedest}\n
        8. System Flag Fraud Status: {isflaggedfraud}
                    """)

        if int(prediction) == 1:
            st.error(f"### The '{x}' transaction between {sender_name} and {receiver_name} is **fraudulent**.")
        else:
            st.success(f"### The '{x}' transaction between {sender_name} and {receiver_name} is **not fraudulent**.")

    st.write("Developed by: Oduyebo oluwatobi victor")
