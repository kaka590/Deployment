import streamlit as st
st.title ('Welcome everyone to Gomycode Presentation, Kaka loves you all')
st.write ('this day of presentation 25th September, 2025')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\FB_IMG_1644753037285.jpg")
st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG-20240818-WA0010.jpg")
st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Gunna-forever-be-mine-ft-Wizkid-(JustNaija.com).mp3")

Church = st.selectbox('Church', ['Catholic Church Of Visitation'])
RequirementsForChurchBuilding = st.selectbox('RequirementsForChurchBuilding', ['Chairs', 'Zincs', 'Granites', 'Interlocks', 'Windows', 'ReverendsHouse', 'Gate', 'Blocks', 'Sand'])
Chairs = st.number_input('Chairs Expectation, value=0')
Zincs = st.number_input('Zinc Expectation, value=0')
Granite = st.number_input('Granite Expectation, value=0')
Interlocks = st.number_input('Interlocks Expectation, value=0')
Windows = st.number_input('Windows Expectation, value=0')
ReverendsHouse = st.number_input('ReverendsHouse Expectation, value=0')
Gate = st.selectbox('Gate Expectation', ['3 million naira only'])
Blocks = st.number_input('Blocks Expectation, value=0')
Sand = st.number_input('Sand Expectation, value=0')
Expectation = st.selectbox('Expectation', '55 miliion naira')

if st.button('CHURCH BUILDING PROJECT'):
    Chairs > 1350000 and Zincs > 550000 and Granite > 640000 and Interlocks > 700000 and Windows > 300000 and ReverendsHouse > 4000000 and Blocks > 370000 and Sand > 399999 
    st.success(f'Lets go on with the expectation, (Chairs:{Chairs}, (Zincs:{Zincs}, (Granite:{Granite}, (Interlocks:{Interlocks}, (Windows:{Windows}, (ReverendsHouse:{ReverendsHouse}, (Blocks:{Blocks}, (Sand:{Sand} OK LETS START BUILDING')
    st.error(f'Dont go on with this, (Chairs:{Chairs}, (Zincs:{Zincs}, (Granite:{Granite}, (Interlocks:{Interlocks}, (Windows:{Windows}, (ReverendsHouse:{ReverendsHouse}, (Blocks:{Blocks}, (Sand:{Sand} DONT START BUILDING')