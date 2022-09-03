import streamlit as st
import pandas as pd

st.title('Dashboard')

df = pd.read_csv('data/pub.csv')


df_radio = st.radio("Select the retrieval option",("Postalcode","LocalAuthority"),horizontal=True)

if df_radio == "Postalcode":
    df_shw = st.selectbox(
        'Select Postal code',
        df["postcode"].unique())

    st.map(df[df["postcode"] == df_shw])

else:
    df_shw = st.selectbox(
        'Select Local Authority',
        (df["local_authority"].unique()))

    st.map(df[df["local_authority"] == df_shw])


