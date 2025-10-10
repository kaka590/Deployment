import streamlit as st
st.title ('GOOD NIGHT EVERYONE WELCOME TO MY CODING TUTORIAL BEFORE SLEEPING')
st.write ('I LOVE STREAMING GUYS GIFT ME TO ENCOURAGE THIS CODING')

def code():
    return 'Kaka'

st.subheader('image')    ####### NOT CALLED PHOTO OR PICTURE ITS CODING WORD IS (IMAGE)
st.image(r"C:\Users\USER\OneDrive\Bilder\FB_IMG_1644753037285.jpg")

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241025_233023_098.jpg")

st.subheader ('audio')    ###### In creating app the word is (audio) not MUSIC OR SONG
st.audio(r"C:\Users\USER\Music\Juice-WRLD-–-Wishing-Well-via-Naijafinix.com_.mp3")

st.subheader ('video')
st.video (r"C:\Users\USER\Videos\Screen Recordings\8a144c1cd2f535257006dad994c33548-1.mp4")

st.subheader('file_uploader')
st.file_uploader(r"C:\Users\USER\OneDrive\Desktop\Deployment\main.py")

st.title ('SS1 MATHEMATICS CHECK AND GRADING FOR ONLY MATHEMATICS')
Class = st.selectbox('Class', ['Senior Secondary Class(SS1A)', 'Senior Secondary Class(SS1B)'])
Subject = st.selectbox('Subject', ['Maths'])
Excellent = st.number_input('Excellent', value=0)
V_Good = st.number_input('V_Good', value=0)
Good = st.number_input('Good', value=0)
Fair = st.number_input('Fair', value=0)
Failed = st.number_input('Failed', value=0)
Students_name = st.text_input('Students_name')

if st.button('MATHS PERFORMANCES AND GRADING'):
    Excellent >89 
    V_Good >75<88
    Good >60<74
    Fair >49<59
    Failed >0<48
    st.success(f'THESE ARE THE MATHS PERFORMANCES IN SS1 CLASS BEST IN MATHS WAS GOTTEN FROM Excellent, (Excellent:{Excellent}, (V_Good:{V_Good}, (Good:{Good}, (Fair:{Fair}, (Failed:{Failed} ANY STUDENT WHO GOT EXCELLENT AND V_Good WAS EXCEPTIONALLY GREAT')
    st.error(f'THESE ARE THE MATHS PERFORMANCES IN SS1 CLASS NON OF THEM WERE THE BEST EXCEPT THE STUDENT WITH EXCELLENT, (Excellent:{Excellent}, (V_Good:{V_Good}, (Good:{Good}, (Fair:{Fair}, (Failed:{Failed} JUST A NORMAL PERFORMANCE BY THE STUDENT')
    