import streamlit as st
st.title ('Welcome all to my Gomycode presentation day')
st.write ('enjoy coding effortlessly with kaka')

def code():
    return 'Kaka'

st.subheader('image')
st.image(r"C:\Users\USER\OneDrive\Bilder\IMG_20241020_005544_543.jpg")

st.subheader('audio')
st.audio(r"C:\Users\USER\Music\Burna_Boy_-_Ye.mp3")

### I want to creat a model where i will have all the recipe and preparation of Nigerian foods to us all

st.title ('KAKA KITCHEN RECIPE AND PROCEDURES FOR COOKING APP')

Foods = st.selectbox('Foods', ['Ogbonno', 'Egusi', 'Stew', 'Peppersoup', 'FriedRice', 'Jollof Rice'])
OgbonnoIngredients = st.selectbox('OgbonnoIngredients', ['Ogbonno seed', 'Ogili', 'Cray fish', 'Meat', 'Stockfish', 'Chicken', 'RedOil', 'Vegetable', 'Maggi', 'Salt'])
OgbonnoPreparation = st.selectbox('OgbonnoPreparation', ['Boil meat water with salt maggi and onions', 'After boiling Pour adequate amount of Redoil with Ogbonno Crayfish and small ogili inside the pot', 'Taste the soup add any missing thing like salt maggi etc', 'Finally put Vegetable in the soup and wait till is ready'])

EgusiIngredient = st.selectbox('EgusiIngredent', ['Egusi seed', 'Ogili', 'Meat', 'Stockfish', 'Chicken', 'RedOil', 'Vegetable', 'Maggi', 'Salt'])
EgusiPreparation = st.selectbox('EgusiPreparation', ['Boil meat water with salt maggi and onions', 'after boiling Pour adequate amount of Redoil with Grinded Egusi Crayfish and small ogili inside the pot', 'Taste the soup add any missing thing like salt maggi etc', 'Finally put Vegetable in the soup and wait till is ready'])

StewIngredient = st.selectbox('StewIngredient', ['Sachet tomatoes or Fresh Tomatoes', 'Fresh Pepper or Gringed Pepper', 'Meat chicken or Fish', 'Groundnut oil', 'Maggi', 'Salt', 'Water', 'Thyme', 'Curry','Onga'])
StewPreparation = st.selectbox('StewIngredent', ['Boil the already grinded tomatoes pepper onions and shombo till it is dried', 'Buy your MEAT CHICKEN OR FISH WASH AND COOK IT WITH MAGGI SALT THYME CURRY etc', 'Fry meat or fish or chicken after Boiling', 'Use that same Groundnut oil you used to fry the chicken to fry your boiled tomatoes', 'Pour all the meat water in the frying Tomatoes', 'Taste and add any missing recipe if noticed eg salt maggi onions etc', 'Wait till it is dried then it is ready'])

PeppersoupIngredients = st.selectbox('Peppersoup_Ingredients', ['Pepper', 'Salt', 'Maggi', 'Peppersoup spices', 'water', 'Pounded yam or coco yam for thickness', 'Onions', 'small_leaf utazi or ugu'])
PeppersoupPreparation = st.selectbox('PeppersoupPreparation', ['NOT COMPULSORY for thickness boil yam or cocoyam then pound it scope it out in a plate then', 'Boil your chicken meat or catfish with onions alot of pepper maggi salt and peppersoup spice', 'For thickening the pepersoup put adequate amount of pounded yam or cocoyam in the cooking pot till you get staified with thickness', 'Put selected leaf like ugu scent leaf etc then wait till the soup is ready'])

FriedRiceIngredients = st.selectbox('FriedRiceIngredients', ['Rice', 'Maggi', 'Salt', 'Pepper', 'Curry', 'Thyme', 'Onions', 'Water', 'FriedRice spice or Spicity', 'Chicken Turkey fish etc'])
FriedRicePreparation = st.selectbox('FriedRicePreparation', ['Boil rice and keep aside', 'Boil meat with water salt maggi onions curry thyme meat spices add fried rice spices', 'fry your meat fish chicken', 'Now pour all the boiled rices into the cooking meat water add any spices of your choice if needed wait till its ready'])


JollofRiceIngredients = st.selectbox('FriedRiceIngredients', ['Rice', 'Meat Fish Chicken Thurkey etc', 'Maggi', 'Salt', 'Curry', 'Thyme', 'Tomotoes fresh or Sachet tomatoes', 'Pepper fresh or Sachet tomatoes', 'Onions', 'Onga Jollof spices of any choice of yours'])
JollofRicePreparation = st.selectbox('JollofRicePreparation', ['Boil Rice Keep the rice aside', 'Fry stew with tomatoes chicken meat fish turkey', 'add water in the stew then pour the boiled rice in the stew you cooked preare food till its tasty', 'add any maggi salt or jollof spice if needed then wait till the food is ready'])

Remarks = st.selectbox('Remarks', ['SATISFIED', 'UNSATISFIED'])

Workers_Words = st.text_input('Managers_Words')

if st.button ('KAKAS RESTURANTS'):
    Remarks == 'SATISFIED'
    st.success(f'When worker selects SATSIFIED the cooking menu was simple and followed, (Foods:{Foods}, (OgbonnoIngredients:{OgbonnoIngredients}), (OgbonnoPreparation:{OgbonnoPreparation}), (EgusiIngredients:{EgusiIngredient}, (EgusiPreparation:{EgusiPreparation}, (StewIngredient:{StewIngredient}, (StewPreparation:{StewPreparation}, (PepersoupIngredients:{PeppersoupIngredients}, (PeppersoupPreparation:{PeppersoupPreparation}, (FriedRiceIngredients:{FriedRiceIngredients}, (FriedRicePreparation:{FriedRicePreparation}, (JollofRiceIngredients:{JollofRiceIngredients}, (JollofRicePreparation:{JollofRicePreparation} RECEIPY WAS FOLLOWED AND USED BY WORKER IN MY KITCHEN')
    st.error(f'When worker selects UNSATSIFIED the cooking menu was not simple and followed, (Foods:{Foods}, (OgbonnoIngredients:{OgbonnoIngredients}), (OgbonnoPreparation:{OgbonnoPreparation}), (EgusiIngredients:{EgusiIngredient}, (EgusiPreparation:{EgusiPreparation}, (StewIngredient:{StewIngredient}, (StewPreparation:{StewPreparation}, (PepersoupIngredients:{PeppersoupIngredients}, (PeppersoupPreparation:{PeppersoupPreparation}, (FriedRiceIngredients:{FriedRiceIngredients}, (FriedRicePreparation:{FriedRicePreparation}, (JollofRiceIngredients:{JollofRiceIngredients}, (JollofRicePreparation:{JollofRicePreparation} RECEIPY WAS NOT FOLLOWED AND USED BY WORKER IN MY KITCHEN')
    