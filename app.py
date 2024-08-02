# app.py
import streamlit as st
from bank import Bank

# Path to your logo image
logo_path = "transaction.jpg"

# Initialize the bank account with an initial balance of 0.00
account = Bank()

# Display the logo
st.image(logo_path, width=200)  # Adjust width as needed

st.title("Bank Transaction App")

action = st.radio("Select Action:", ("Deposit", "Withdrawal"))

amount = st.text_input("Enter the amount:")

if st.button("Submit"):
    try:
        amount = float(amount)
        if action == "Deposit":
            success, result = account.deposit(amount)
            if success:
                st.success(f"Deposited: {amount}")
                st.info(f"Your account balance: {result}")
            else:
                st.error(result)
        elif action == "Withdrawal":
            success, result = account.withdrawal(amount)
            if success:
                st.success(f"Withdrew: {amount}")
                st.info(f"Your account balance: {result}")
            else:
                st.error(result)
    except ValueError:
        st.error("You have entered an invalid input. Please try again with a numerical value.")

if st.button("Show Transaction Log"):
    try:
        with open("transaction.txt", "r") as file:
            st.text(file.read())
    except FileNotFoundError:
        st.error("No transaction log found.")

if st.button("Clear Transaction Log"):
    with open("transaction.txt", "w") as file:
        file.write("")
    st.success("Transaction log cleared.")
