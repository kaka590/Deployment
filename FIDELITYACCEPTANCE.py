import streamlit as st
st.title('Time is not on our side eh')
st.write ('A quick project on my own')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241020_005508_362.jpg")

st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Kvng-Vinci-Squid-Game-Amapiano-Remix--(BeatzJam.com).mp3")

st.subheader('video')
st.video(r"C:\Users\USER\Videos\Screen Recordings\Screen Recording 2025-05-24 003001.mp4")

st.subheader('file_uploader')
st.file_uploader(r"C:\Users\USER\OneDrive\Dokumente\online_furniture_retailer.csv")

Fidelity = st.selectbox('Fidelity', ['Cashier', 'Customer_service', 'DSA', 'SMA', 'Operators', 'Manager'])
Salary =st.number_input('Salary')
official_wears = st.selectbox('official_wears', ['Black_suites', 'Corperate polos', 'Boots'])
Days_of_Work = st.selectbox('Days_of_Work', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
managers_briefing = st.text_input('managers briefing')
office_hours = st.selectbox('office_hours/closing', ['8am till 5pm'])
JOB_APPLICANT = st.text_input('JOB APPLICANT NAME')

if st.button('Conditions to work'):
    Fidelity == 'Cashier' and Salary == 190000 and official_wears == 'Black_suites'
    Fidelity == 'Customer_service' and Salary == 160000 and official_wears == 'Black_suites'
    Fidelity == 'DSA' and Salary == 130000 and official_wears == 'Black_suites'
    Fidelity == 'SMA' and Salary == 150000 and official_wears == 'Black_suites'
    Fidelity == 'Operators' and Salary == 250000 and official_wears == 'Black_suites'
    Fidelity == 'Manager' and Salary == 900000 and official_wears == 'Black_suites'
    
    st.success(f'Once applicant agrees to this processof the employment employ the person,(Fidelity:{Fidelity}, (Salary:{Salary}, (official_wear:{official_wears}, (Days_of_Work:{Days_of_Work}, (managers_briefing:{managers_briefing}, (office_hours:{office_hours}, (Job_APPLICANT:{JOB_APPLICANT}  ACCEPT THIS PERSON INSTANTLY')
    st.errors(f'Once applicant does not agrees to this process the employment dont employ,(Fidelity:{Fidelity}, (Salary:{Salary}, (official_wear:{official_wears}, (Days_of_Work:{Days_of_Work}, (managers_briefing:{managers_briefing}, (office_hours:{office_hours}, (Job_APPLICANT:{JOB_APPLICANT}  DONT ACCEPT THIS PERSON INSTANTLY')
