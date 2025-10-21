import streamlit as st
st.title ('GOOD NIGHT CODING')
st.write ('ALOT OF ACTIVITIES MAKE WE JUST CODE BA')

def code():
    return 'Kaka'

st.subheader('file_uploader')
st.file_uploader(r"C:\Users\USER\OneDrive\Dokumente\fashion_boutique_dataset.csv")

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241020_005745_449.jpg")

st.subheader('video')
st.video(r"C:\Users\USER\Videos\Screen Recordings\58b19a675c856c1da541c8146e2fdce9.mp4")

age = st.number_input('age', value=0)
PARTY_TYPE = st.selectbox('PARTY TYPE', ['ADULTS NIGHT OUT'])
Dress_Code = st.selectbox('Dress_Code', ['Bikinis', 'BLACK SHADES', 'White band', 'FOR MEN NIGHT GOWN'])
Gender = st.selectbox('Gender', ['Male', 'Female'])
Note_by_celebrant = st.text_input('Note_by_celebrant')

if st.button('PARTY ALL NIGHT'):
    age >18<51
    PARTY_TYPE == 'ADULTS NIGHT OUT'
    st.success(f'THIS PERSON WILL BE GRANTED ACCESS INSTANTLY, (age:{age}, (PARTY_TYPE:{PARTY_TYPE} ENTER THE PARTYING HALL')
    st.error(f'THIS PERSON WILL NOT BE GRANTED ACCESS, (age:{age}, (PARTY_TYPE:{PARTY_TYPE} DONT ENTER THE PARTYING HALL')
    