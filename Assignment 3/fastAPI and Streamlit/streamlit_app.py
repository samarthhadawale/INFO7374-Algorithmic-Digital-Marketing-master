import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import json,requests

st.sidebar.markdown('**_RECOMMENDATION SYSTEM :SNACKFAIR_**')
itemName = pd.read_csv('data/itemInfo.csv')
userName = pd.read_csv('data/userData.csv')

radio = st.sidebar.radio(
    "Select an Algorithm from below List to see the Recommendations!",
    ("LightFM Algorithm","LightGBM Algorithm")
#st.markdown('<style>body{background-color: #B8E2F2;}</style>',unsafe_allow_html=True)
#st.sidebar.slider.markdown("<h1 style='text-align: left; color: Blue;'>'ABC',0,20,10</h1>", unsafe_allow_html=True)
)

st.markdown('<style>body{background-color: #FFF2C2;}</style>',unsafe_allow_html=True)

if radio == 'LightFM Algorithm':
    
    genre = st.selectbox(
        "Choose the Recommendation Method among the LightFM Algorithm :",
        ('No Selection','Similarity on the Basis of USER ID', 'Similarity on the Basis of ITEM ID'))
    
    if genre == 'No Selection':
        
        st.title('**_SNACKFAIR Welcomes you to their own Recommendation System!_**')
        image = Image.open('snacks.jpg')
        st.image(image, caption='',use_column_width=True)
    
    
    
    elif genre == 'Similarity on the Basis of USER ID':
        st.title('_Recommendation on the basis of User ID_')
        sentence = st.text_input('Enter the USER ID to get Similar User Details of it:',value='0')
        number = int(sentence)    
        if st.button('Recommend the closest User Details'):
            payload = json.dumps({
                "userID" : number
                })
            response = requests.get(f"http://127.0.0.1:8000/recommend_users?userID={number}")
            data_list = response.json()
            user = pd.DataFrame(data_list)
            user.columns = ['userID']
            user['userID'] = user['userID'].astype(int)
            join = pd.merge(left = user, right = userName, left_on = 'userID', right_on = 'userID')
            join.drop('occupation', axis = 1, inplace = True)
            #join.columns = ['itemID', 'itemName', 'category']

            st.write(join)
    
    
    elif genre == 'Similarity on the Basis of ITEM ID':
        
        st.title('_Recommendation on the basis of Item ID_')
        sentence = st.text_input('Enter the ITEM ID to get Similar Item Details or User Details on the basis of it:',value='0')
        
        number = int(sentence)   
        
        if st.button('Recommend the closest Item Details'):
            payload = json.dumps({
                "itemID" : number
                })
            response = requests.get(f"http://127.0.0.1:8000/recommend_items?itemID={number}")
            data_list = response.json()
            data_list = response.json()
            item = pd.DataFrame(data_list)
            item.columns = ['itemID']
            item['itemID'] = item['itemID'].astype(int)
            join = pd.merge(left = item, right = itemName, left_on = 'itemID', right_on = 'itemID')
            join.drop('category', axis = 1, inplace = True)
            #join.columns = ['itemID', 'itemName', 'category']
            
            st.dataframe(join)
            #st.markdown(data_list)
            
            
        if st.button('Recommend the closest User Details'):
            payload = json.dumps({
                "itemID" : number
                })
            response = requests.get(f"http://127.0.0.1:8000/recommend_items_users?itemID={number}")
            data_list = response.json()
            user = pd.DataFrame(data_list)
            user.columns = ['userID']
            user['userID'] = user['userID'].astype(int)
            join = pd.merge(left = user, right = userName, left_on = 'userID', right_on = 'userID')
            join.drop('occupation', axis = 1, inplace = True)
            #join.columns = ['itemID', 'itemName', 'category']
            
            st.dataframe(join)

if radio == 'LightGBM Algorithm':
    
    
    #st.title('**_SNACKFAIR Welcomes you to their own Recommendation System!_**')
    #image = Image.open('snacks.jpg')
    #st.image(image, caption='',use_column_width=True)
    st.title('_Recommendation on the basis of User ID_')
    
    title = st.number_input('Enter the USER ID to get Similar Item Details',min_value = 450000,max_value=900000,value = 450000,step =1)
    
    if st.button('Recommend the closest Item Details'):
        data = pd.read_csv('test_data.csv')
        df1 =  data['id']==title
        df2 = data[df1]
        data = pd.DataFrame(df2) 
        st.dataframe(data['product_cat'])
    
    if st.button('Estimation of prospect buyer'):
        data = pd.read_csv('test_data_new.csv')
        df1 = data['id'] == title
        df2 = data[df1]
        
        if(int(df2['Action']) == 1):
            st.write('User will probably end up buying something!')
        elif(int(df2['Action']) == 0):
            st.write('Most probably user will not buy anything!')
            
        
        
    
            
    
    