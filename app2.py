import streamlit as st

st.write("""
# Finding largest of 3 given numbers
This app finds the value greater than other two numbers
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

sum = [data['First_Number']+data['Second_Number']]

#Output

st.subheader('Greatest number among the given inputs is:')
st.write(sum)
