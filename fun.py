import streamlit as st
st.title ('ENJOY CODING TO THE FULLEST WITH KAKA')
st.write ('A cryptocurrency analysis')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\WhatsApp Image 2025-09-02 at 16.22.13_ed0dfb5d.jpg")
st.subheader('audio')
st.audio(r"C:\Users\USER\Music\ATLXS_-_PASSO_BEM_SOLTO_-_Slowed_@BaseNaija.mp3")

cryptocurrencies =st.selectbox('cryptocurrencies', ['Algorand', 'Avalanche', 'Bitcoin', 'Cardano', 'Cosmos', 'Chainlink', 'Etherium', 'Polkadot', 'Polygon', 'Solana'])
Values = st.number_input('Place the choice of value to dataset, value=0')
message = st.text_input('drop a text here')

if st.button('Crypto'):
    {cryptocurrencies} and Values > 39
    st.success(f'when cryptocurrencies are at value > 39 it is valueable, (cryptocurrencies:{cryptocurrencies}, (Value:{Values}, (message:{message} Let us invest in this crypto abeg')
    st.error(f'when cryptocurrencies are at value < 39 it is valueless to us, (cryptocurrencies:{cryptocurrencies}, (Value:{Values}, (message:{message} avoid this crypto abeg')
