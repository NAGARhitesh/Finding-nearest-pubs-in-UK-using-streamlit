import streamlit as st
import pandas as pd

st.title("Nearest pub")
df = pd.read_csv('data/pub.csv')


x1 = st.number_input("Enter the latitude of your location",format="%.6f")
y1 = st.number_input("Enter the longitude of your location",format="%.6f")

a = df["latitude"]
b = df["longitude"]
distance = []
for i,j in zip(a,b):
    distance.append(((i-x1)**2+(j-y1)**2)**1/2)
df["distance"] = distance
st.map(df.sort_values(by="distance").head(6).iloc[1:])

