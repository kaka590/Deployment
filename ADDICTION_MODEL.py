import streamlit as st
st.title('I WELCOME YOU ALL TO MY PRESENTATION ON THE 12TH OF SEPTEMBER, 2025')
st.write('Everybody loves kaka welcome to my world')

def code():
    return 'Kaka'

##### I want to launch this app teaching people you all on how to upload image, video and audio in creation of applications

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\Screenshot_20230622-142352.png")

st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Dj_Maphorisa_x_Wizkid_Good_Love_Prod_by_Nana_Rouges_9jaflaver.com_.mp3")

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\FB_IMG_1644753037285.jpg")


###### Now, I would like to Create my model, create a button for it, fit the model, then select the (SUCCESS AND FAILURES IN THE APP)

## i HAVE CREATED THE MODEL HERE
write_ups = st.text_input('Put in some wtie_ups')
gender = st.selectbox('gender', ['Others', 'Male', 'Female'])
country = st.selectbox('country', ['Yemen', 'Saudi Arabia', 'Togo', 'Morroco', 'Jamaica', 'Macedonia', 'Bermuda', 'Falkland Islands (Malvinas)'])
city = st.selectbox('city', ['Martinmouth', 'Chanport', 'Harperhaven', 'Danielberg', 'North Cory', 'Port Kimberly', 'smithbury', 'Clinebury', 'Colleenport', 'Turnertown'])
smokes_per_day = st.number_input('smokes_per_day, value=0')
drinks_per_week = st.number_input('drinks_per_week, value=0')
age_started_smoking = st.number_input('age_started_smoker, value=0')
age_started_drinking = st.number_input('age_started_drink, value=0')
attempts_to_quit_smoking = st.number_input('attempts_to_quit_smoking, value=0')
attempts_to_quit_drinking = st.number_input('attempts_to quit_drinking, value=0')
has_health_issues = st.selectbox('has_health_issues', ['True', 'False'])
mental_health_status = st.selectbox('mental_health_status', ['Good', 'Poor', 'Average'])


if st.button('ADDICTION LEVEL PREDICTION'):
    has_health_issues == 'False' and mental_health_status == 'Good'
    st.success(f'When the person does not have_health_issue as and mental_health_status is Good the persons addiction is not critical to kill him, (write_ups:{write_ups}, (gender:{gender}, (country:{country}, (city:{city}, (smokes_per_day:{smokes_per_day}, (drinks_per_week:{drinks_per_week}, (age_started_drinking:{age_started_drinking}, (age_started_smoking:{age_started_smoking}, (attempts_to_quit_smoking:{attempts_to_quit_smoking}, (attempts_to_quit_drinking:{attempts_to_quit_drinking}, (has_health_issues:{has_health_issues}, (mental_health_status:{mental_health_status} THE PERSONS ADICTION IS NOT TOO CRITICAL TO KILL HIM/HER YET')
    st.error(f'When the person health_issue is True and mental_health_status are both Average and poor the persons addiction is too critical to kill him,(write_ups:{write_ups}, (gender:{gender}, (country:{country}, (city:{city}, (smokes_per_day:{smokes_per_day}, (drinks_per_week:{drinks_per_week}, (age_started_drinking:{age_started_drinking}, (age_started_smoking:{age_started_smoking}, (attempts_to_quit_smoking:{attempts_to_quit_smoking}, (attempts_to_quit_drinking:{attempts_to_quit_drinking}, (has_health_issues:{has_health_issues}, (mental_health_status:{mental_health_status} THE PERSONS ADICTION IS TOO CRITICAL TO KILL HIM/HER ADVISE THE PERSON TO STOP AND PRAY TO GOD ON HIS/HER LIFE')