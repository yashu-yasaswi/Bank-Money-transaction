# app.py
import streamlit as st
from bank import Bank

# Initialize the bank account with an initial balance of 0.00
account = Bank()

st.title("Bank Transaction App")

action = st.radio("Select Action:", ("Deposit", "Withdrawal"))

amount = st.text_input("Enter the amount:")

if st.button("Submit"):
    if action == "Deposit":
        account.deposit(amount)
        st.success(f"Deposited: {amount}")
    elif action == "Withdrawal":
        account.withdrawal(amount)
        st.success(f"Withdrew: {amount}")
    st.info(f"Your account balance: {account.balance}")

if st.button("Show Transaction Log"):
    try:
        with open("transaction.txt", "r") as file:
            st.text(file.read())
    except FileNotFoundError:
        st.error("No transaction log found.")
