import numpy as np
import streamlit as st
import pickle
import pandas as pd
cars=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv("Cleaned_Car_data.csv")

companies= sorted(car['company'].unique())


st.title('Car Price Prediction')
option1 = st.selectbox('Select the brand',companies)

st.write('You selected:', option1)
model = car["name"].loc[car["company"] == option1]
option2 = st.selectbox( 'Select the model', model)

st.write('You selected:', option2)
fuel_type= sorted(car['fuel_type'].unique())
option3 = st.selectbox('Select the fuel type', fuel_type)

st.write('You selected:', option3)

year= sorted(car['year'].unique())
option4 = st.selectbox('Select the Year', year)

st.write('You selected:', option4)
Km_driven= st.slider(
    'Select a range of values',
    0, 60000)
st.write('Kilometers Driven:', Km_driven)

prediction=cars.predict(pd.DataFrame([[option2,option1,option4,Km_driven,option3]],columns=['name','company','year','kms_driven','fuel_type']))
predict=str(np.round(prediction[0],2))
if st.button('Predict',type='primary'):
    st.write('Rs.',predict)
