
import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.write("""
Sum of two numbers
""")

st.header('User Input')

def user_input_features():
  number_1=st.number_input("First_number",min_value=None,max_value=None)
  number_2=st.number_input("Second_number",min_value=None,max_value=None)
  data = {'First number': number_1,
      'Second number':number_2}
  features=pd.DataFrame(data,index=[0])
  return features

df=user_input_features()

sum=df.add

st.write(sum)
