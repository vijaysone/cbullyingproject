import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle

new_title = '<p style="font-family:sans-serif; color:skyblue; font-size: 42px;">Cyberbulling Tweet Recognition App</p>'
st.markdown(new_title, unsafe_allow_html=True)


__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')
                    

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
        image = Image.open('images/logo.png')

        st.image(image, use_column_width= True)

        st.write('''
    
    This app predicts the nature of the tweet into 6 Categories.
    * Age
    * Ethnicity
    * Gender
    * Religion
    * Other Cyberbullying
    * Not Cyberbullying

    ***
    ''')

    # Text Box
        st.header('Enter Tweet ')
        tweet_input = st.text_area("Tweet Input", height= 150)
        print(tweet_input)
        st.write('''
        ***
        ''')

        # print input on webpage
        st.header("Entered Tweet text ")
        if tweet_input:
            tweet_input
        else:
            st.write('''
            ***No Tweet Text Entered!***
            ''')
        st.write('''
        ***
        ''')

        # Output on the page
        st.header("Prediction")
        if tweet_input:
            prediction = custom_input_prediction(tweet_input)
            if prediction == "Age":
                st.image("images/age_cyberbullying.png",use_column_width= True)
            elif prediction == "Ethnicity":
                st.image("images/ethnicity_cyberbullying.png",use_column_width= True)
            elif prediction == "Gender":
                st.image("images/gender_cyberbullying.png",use_column_width= True)
            elif prediction == "Not Cyberbullying":
                st.image("images/not_cyberbullying.png",use_column_width= True)
            elif prediction == "Other Cyberbullying":
                st.image("images/other_cyberbullying.png",use_column_width= True)
            elif prediction == "Religion":
                st.image("images/religion_cyberbullying.png",use_column_width= True)
        else:
            st.write('''
            ***No Tweet Text Entered!***
            ''')

        st.write('''***''')
