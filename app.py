import streamlit as st
import pandas  as pd
import time
st.title('startup dashboard')
st.subheader('this is streamlit project')
st.subheader('startup project')
st.write('this is a normal line')
st.markdown("""
### My favourite movies 
- 3 idiots
- hasi to fasi
- meri pyari bindu""")
st.code("""
model=Sequential()
model.add(Dense(128,input_dim=2,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
adam=Adam(learning_rate=0.01)
model.compile(loss='binary_crossentropy',optimizer=adam,metrics=['accuracy'])
history=model.fit(X ,y,epochs=500,validation_split=0.2,verbose=False)""")
st.latex('x^2 + y^3 =50')
df=pd.DataFrame
st.metric('revenue','Rs3l','+5%')
st.sidebar.title('sidebar title')
col1,col2=st.columns(2)
with col1:
    st.latex('a+b')
with col2:
    st.code("""
    a=int(input('enter the first number')
    b=int(input('enter the second no'))
    sum=a+b
    print(sum)                """)

st.error('login failed')
st.success('login successful')
bar=st.progress(0)
for i in range(0,101):
    time.sleep(0.1)
    bar.progress(i)

email=st.text_input('email')
number=st.number_input('enter age')
gender = st.selectbox('Select gender',['male','female','others'])
st.success('login success')
df=df.dropna(subset=['date','Startup Name','vertical','city','round','amount'])