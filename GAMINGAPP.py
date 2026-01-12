import streamlit as st
st.title ('GOOD AFTERNOON MR.AJAYI THIS IS MY APP ON GAMES')
st.write ('SIR, FROM VICTOR KAKA')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\Screenshot_20230622-142352.png")

st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Burna_Boy_-_Tested_Approved_Trusted.mp3")

st.subheader('video')
st.video(r"C:\Users\USER\Videos\Screen Recordings\509a3427946f403db3b6b8f052454abc.mp4")

Gender = st.selectbox('Gender', ['Male', 'Female'])
Location = st.selectbox('Location', ['Other', 'USA', 'Europe', 'USA', 'Asia', 'Europe', 'Other'])
GameGenre = st.selectbox('GameGenre', ['Strategy', 'Strategy', 'Sports', 'Action', 'Action', 'RPG', 'Action', 'RPG', 'Simulation', 'Sports'])
GameDifficulty = st.selectbox('GameDifficulty', ['Medium', 'Easy', 'Hard'])
PlayerLevel = st.number_input('PlayerLevel', value=0)
AchievementsUnlocked = st.number_input('AchievementsUnlocked', value=0)
EngagementLevel = st.selectbox('EngagementLevel', ['Medium', 'High', 'Low', 'High'])

if st.button('GAME ANALYSIS APP AND APPLICATION MANAGEMENT'):
    EngagementLevel == 'High'
    st.success(f'THIS MEANS THIS PERSON IS ADDICTED TO THIS PATTERN OR GENRE IN GAMING, (EngagementLevel:{EngagementLevel} ADDICTED AND FAVOURITE GAME HE/HER PLAYS')
    st.error(f'THIS MEANS THE PERSON PLAYS THIS GENRE FREQUENTLY NOT OFTEN, (EngagementLevel:{EngagementLevel} HE/HER IS NOT YET ADDICTED TO THIS GAME YET')
