import streamlit as st
import pandas as pd

st.title('Homepage')

df=pd.read_csv('data/pub.csv')
df=df.drop(['Unnamed: 0'],axis=1)



a1=st.radio("upper data or lower data",
("Head",'Tail'))

if a1=='Head':
    st.dataframe(df.head())
elif a1=='Tail':
    st.dataframe(df.tail())  

a2=st.radio("explore the data",
("Columns","Shape"))

if a2 == 'Columns':
    st.text(df.columns)
elif a2 == 'Shape':
    st.text('Number of rows: {}'.format(df.shape[0]))
    st.text('Number of Cols: {}'.format(df.shape[1]))
