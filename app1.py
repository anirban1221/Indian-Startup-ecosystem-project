import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('startup_cleaned1.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')

def load_investor_details(investor):
    st.title(investor)
    recent_inv=df[df['investors'].str.contains(investor)].head(10).drop(columns=['SubVertical','investors'])
    st.subheader('most recent investments')
    st.dataframe(recent_inv)
    col1,col2=st.columns(2)
    with col1:
        big_inv=df[df['investors'].str.contains(investor)].groupby('Startup Name')['amount in cr(INR)'].sum().sort_values(ascending=False).head() 
        st.subheader('top investments')
        st.dataframe(big_inv)
        st.bar_chart(data=recent_inv, x='Startup Name', y='amount in cr(INR)', color=None, horizontal=False,
                     stack=None, width=None, height=None, use_container_width=True)
    with col2:
        vertical_inv=df[df['investors'].str.contains(investor)].groupby('vertical')['amount in cr(INR)'].sum().sort_values(ascending=False).head(7)
        st.subheader('Sectors invested in')
        fig1=plt.figure(figsize=(4,4))
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_inv,labels=vertical_inv.index,autopct="%0.01f%%",radius=1)
        st.pyplot(fig1)
    
    top_cities=df[df['investors'].str.contains(investor)].groupby('city')['amount in cr(INR)'].sum().sort_values(ascending=False).head() 
    st.subheader('top locations')
    st.bar_chart(data=recent_inv, x='city', y='amount in cr(INR)', color=None, horizontal=False,
                 stack=None, width=None, height=None, use_container_width=True)
    
    df['year'] = df['date'].dt.year
    trend=df[df['investors'].str.contains(' IDG Ventures')].groupby('year')['amount in cr(INR)'].sum()
    trend_df = trend.reset_index()
    trend_df.columns = ['year', 'amount in Cr(INR)']
    st.subheader('Investment trend in recent years')
    st.line_chart(data=trend_df, x='year', y='amount in Cr(INR)', x_label=None, y_label=None, 
                  color=None, width=None, height=None, use_container_width=True) 

st.sidebar.title('startup funding analysis')
option=st.sidebar.selectbox('select one',['overall analysis','startup','investor'])
if option=='overall analysis':
    st.title('overall analysis')
elif option=='startup':
    st.sidebar.selectbox('select startup',sorted(df['Startup Name'].unique().tolist()))
    st.title('startup analyis')
else:
    selected_investor=st.sidebar.selectbox('Select investor',sorted(set(df['investors'].str.split(',').sum())))
    st.title('investor analyis')
    btn2=st.sidebar.button('find investor details')
    if btn2:
        load_investor_details(selected_investor)
   