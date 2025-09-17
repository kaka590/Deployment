import streamlit as st
st.title ('GOOD MORNING ALL TODAY 18TH SEPTEMBER 2025 IS MY PRESENTATION ENJOY TO THE FULLEST')
st.write ('I feel i am chosen i am covered in Gold')

def code():
    return 'Kaka'

st.subheader('file_uploader')
st.file_uploader(r"C:\Users\USER\OneDrive\Dokumente\Mall_Customers.csv")

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241020_005436_774.jpg")

Gender = st.selectbox('Gender', ['Male', 'Female'])
Age = st.number_input('AGE')
Spending_Score_1_TO_100 = st.number_input('SPENDING_SCORE_1_TO_100')
name = st.text_input('Name of person')

if st.button('Spending Habit'):
    Spending_Score_1_TO_100 > 65
    st.success(f'anybody that has spending habit of 65% and above hardly saves, (Spending_Score_1_TO_100:{Spending_Score_1_TO_100} THIS PERSON IS FUND OF SPENDING CARELESSLY AND HAS A HABIT OF CARELESS SPENDING')
    st.success(f'anybody that has spending habit below 65% hardly saves, (Spending_Score_1_TO_100:{Spending_Score_1_TO_100} THIS PERSON IS NOT FUND OF SPENDING CARELESSLY AND HAS A HABIT OF SPENDING')