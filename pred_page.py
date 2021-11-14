import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('save_step.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

reg = data["model"]

def show_pred_page():
    st.title("King County House Price Prediction")

    st.header("Created By The Bojongers")
    form1 = st.sidebar
    form1.subheader("Insert Input To Predict")
    bedrooms = form1.number_input("Bedrooms",value=int())
    bathrooms = form1.number_input("Bathrooms",value=int())
    floors = form1.radio("Floors",[1,2,3])
    sqft_lot = form1.number_input("Luas Tanah (ft²)",step=float(1))
    sqft_living = form1.number_input("Luas Rumah (ft²)",step=float(1))
    sqft_above = form1.number_input("Luas Atas Rumah (ft²)",step=float(1))
    sqft_basement = form1.number_input("Luas Basement (ft²)",step=float(1))
    waterfront = form1.radio("Waterfront",['Yes','No'])
    view = form1.radio("View",['Excellent','Very Good','Good','Fair','Poor'])
    grade = form1.slider("Grade",1,13,13)
    lat = form1.number_input("Latitude",step=float(1))
    long1 = form1.number_input("Longtitude",step=float(1))
    submit = form1.button("Predict Now")
    if submit :
        if waterfront == 'Yes':
            waterfront=1
        if waterfront == 'No':
            waterfront=0
        if view == 'Excellent':
            view=4
        if view == 'Very Good':
            view=3
        if view == 'Good':
            view=2
        if view == 'Fair':
            view=1
        if view == 'Poor':
            view=0
        D = np.array([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,grade,sqft_above,sqft_basement,lat,long1]])
        price = reg.predict(D)
        st.subheader(f"The estimated house price is ${price[0]:.2f}")
    
    st.write("For more information about this project, check out our [github repository](https://github.com/NicholasHD/TheBojongersHousePredictionApp)")
    
        