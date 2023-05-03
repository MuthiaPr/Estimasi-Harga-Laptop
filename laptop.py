import pickle
import streamlit as st
import numpy as np


df = pickle.load(open('estimasi_laptop_price.sav', 'rb'))

st.title('Estimasi Harga Laptop')

ram = st.selectbox('Ram_GB',[2, 4, 6, 8, 12, 16, 24, 32, 64])

weight = st.number_input('Weight_KG')

touchscreen = st.selectbox('Touchscreen',['No', 'Yes'])

ips = st.selectbox('IPS',['No', 'Yes'])

hdd = st.selectbox('HDD',[0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD',[0, 8, 128, 256, 512, 1024])


if st.button('Predict price'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else: 
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else: 
        ips = 0

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Ram_GB,Weight_KG,TouchScreen,IPS,HDD,SSD]]
    )
    st.write ('Estimasi harga Laptop (euro) : ', predict)
    st.write ('Estimasi harga Laptop (rupiah) :', predict*16216,51)