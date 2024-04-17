import streamlit as st


st.set_page_config(page_title='Calculator', page_icon=':heavy_division_sign:')




st.title('Calculator')
st.divider()


x = st.number_input('Enter the first number:')
y = st.number_input('Enter the second number:')
o = st.selectbox('Enter an operator:', ['multiply', 'subtract', 'add', 'divide'])


if x >= 0.01 and y >= 0.01 and o:
   if st.button('Calculate'):
       if o == 'multiply':
           st.write(f'Your product is: {round(x*y, 2)}')
       if o == 'subtract':
           st.write(f'Your difference is: {round(x-y, 2)}')
       if o == 'add':
           st.write(f'Your sum is: {round(x+y, 2)}')
       if o == 'divide':
           st.write(f'Your quotient is: {round(x/y, 2)}')
