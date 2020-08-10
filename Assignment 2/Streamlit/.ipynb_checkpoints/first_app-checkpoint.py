import streamlit as st
import numpy as np
import pandas as pd

add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("SIMILARITY SEARCH Method", "FAISS Method")
)

st.markdown('<style>body{background-color: #FFFEF2;}</style>',unsafe_allow_html=True)

if add_selectbox == 'SIMILARITY SEARCH Method' :
 st.title("Images using Similarity Search Method")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
    return pd.read_csv('method1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Choose an image from the below list : ")
 pic = st.selectbox('Choices : ', images)
 st.subheader("**_IMAGE_** selected by the **_USER!_**")
 st.image(pic,width=None)
 #st.write('Hello, *World!* :kissing_closed_eyes:')
 #st.subheader("BELOW ARE THE")
 st.subheader('How Many Images do you want to see?')
 z = st.radio(
    'Select the Number',
    (1,2,3,4,5,6,7,8,9,10))
 st.subheader("SIMILAR IMAGES OF THE **_SELECTED IMAGE :_**")
 for index, row in df.iterrows():
     if row['0']==pic:
        while n < z+1:
            st.image(row[n], use_column_width=None, caption=row[n])
            n+=1
            
elif add_selectbox == 'FAISS Method':
 st.title("Images using FAISS Method")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
    return pd.read_csv('faiss.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 st.subheader("Choose an image from the below list : ")
 pic = st.selectbox('Choices:', images)
 st.subheader("**_IMAGE_** selected by the **_USER!_**")
 st.image(pic,width=None)


 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("SIMILAR IMAGES OF THE **_SELECTED IMAGE :_**")
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1


# if genre == '1': 
#     st.image(row[1], use_column_width=None, caption=row[1])
#     #st.write('You selected comedy.')
#     else if genre == '2': 
#     st.image(row[2], use_column_width=None, caption=row[2])
#     #st.write("You didn't select comedy.")

       
