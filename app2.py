import streamlit as st

st.write("""
# Finding sum of two numbers
This app finds the sum of  two numbers
""")
#Get Input

st.header('Input Parameters')


number_1 = st.number_input('Enter first number')
number_2 = st.number_input('Enter second number')
   

data = {'First_Number': number_1,
        'Second_Number': number_2
        }


st.subheader('User Input parameters')
st.write(data)

#Getting largest

sum = data['First_Number']+data['Second_Number']

#Output

st.subheader('Sum of two numbers is :')
st.write(sum)
