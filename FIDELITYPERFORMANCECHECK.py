import streamlit as st
st.title ('Sir LOOK AT THIS QUICK APPLICATION DO YOUR WORK WITH IT AND PREDICT OUR PERFORMANCES')
st.write ('The performance of workers in FIDELITY bank rated by the Branch manager using model')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241020_005745_449.jpg")

st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Major Lazer Ft. Patoranking  Ice Prince  Jidenna   Nasty C – Particula.mp3")

Ada_Customers = st.number_input('Ada_Customers', value=0)
Ada_Customer_Revenue = st.number_input('Ada_customer_Revenue', value=0)
Ada_Position = st.selectbox('Ada_Position', ['ET', 'Assistant Manager', 'Marketer', 'SMA'])
Remark_On_Ada_Report = st.text_input('Give a feedback on how Ada Performed')

Divine_Customers = st.number_input('Divine_Customers', value=0)
Divine_Customer_Revenue = st.number_input('Divine_Customer_Revenue', value=0)
Divne_Position = st.selectbox('Divine_position', ['ET','Assistant Manager', 'Marketer', 'SMA'])
Remark_On_Divine_Report = st.text_input('Give a feedback on how Divine Performed')

Peter_Customers = st.number_input('PETERS_CUSTOMERS', value=0)
Peter_Customer_Revenue = st.number_input('Peter_Customer_Revenue')
Peter_Position = st.selectbox('Peter_position', ['ET', 'Assistant Manager', 'Marketer', 'SMA'])
Remark_On_Peter_Report = st.text_input('Give a feedback on how Peter performed')

Nnnena_Customers = st.number_input('Nnenna_customers', value=0)
Nnnena_Customers_Revenue = st.number_input('Nnenna_Customers_Revenue', value=0)
Nnenna_Position = st.selectbox('Nnenna_position', ['ET', 'Assistant Manager', 'Marketer', 'SMA'])
Remark_On_Nnenna_Report = st.text_input('Give a feedback on Nnenna performance')

Ejike_Customers = st.number_input('Ejike_Customers', value=0)
Ejike_Customers_Revenue = st.number_input('Ejike_Customer_Revenue', value=0)
Ejike_Position = st.selectbox('Ejike_position', ['ET', 'Assistant Manager', 'Marketer', 'SMA'])
Remark_On_Ejike_Report = st.text_input('Give a feedback on Ejike performance')

#### now i want to put a prediction button to help us finalize our model built

if st.button('FIDELITY AT TRINITY APAPA REPORT'):
    Ada_Customers >=12
    Ada_Customer_Revenue > 500000
    Divine_Customers >= 12
    Divine_Customer_Revenue > 500000
    Peter_Customers >=12
    Peter_Customer_Revenue > 500000
    Nnnena_Customers >=12
    Nnnena_Customers_Revenue > 500000
    Ejike_Customers >= 12
    Ejike_Customers_Revenue > 500000
    st.success(f'Target was met and beaten, (Ada_Customers:{Ada_Customers}, (Ada_Customer_Revenue:{Ada_Customer_Revenue}, (Divine_Customers:{Divine_Customers}, (Divine_Customer_Revenue:{Divine_Customer_Revenue}, (Peter_Customers:{Peter_Customers}, (Peter_Customer_Revenue:{Peter_Customer_Revenue}, (Nnenna_Customers:{Nnnena_Customers}, (Nnenna_Customer_Revenue:{Nnnena_Customers_Revenue}, (Ejike_Customers:{Ejike_Customers}, (Ejike_Customers_Revenue:{Ejike_Customers_Revenue} THIS PERSON MET HIS/HER TARGET')
    st.error(f'Target was not met and, (Ada_Customers:{Ada_Customers}, (Ada_Customer_Revenue:{Ada_Customer_Revenue}, (Divine_Customers:{Divine_Customers}, (Divine_Customer_Revenue:{Divine_Customer_Revenue}, (Peter_Customers:{Peter_Customers}, (Peter_Customer_Revenue:{Peter_Customer_Revenue}, (Nnenna_Customers:{Nnnena_Customers}, (Nnenna_Customer_Revenue:{Nnnena_Customers_Revenue}, (Ejike_Customers:{Ejike_Customers}, (Ejike_Customers_Revenue:{Ejike_Customers_Revenue} THIS PERSON DID NOT MET HIS/HER TARGET')