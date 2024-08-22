import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='啟元食品行')

# 頁籤名稱
st.header('公司介紹')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹')
st.sidebar.page_link('pages/page_2.py', label='糖類')

# st.image('https://lh5.googleusercontent.com/p/AF1QipNF0A-hAXYtaPUHDXzESGzBftZsF7spDhSKmLas=s774-k-no')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5, 6, 7],
  'second column': [10, 20, 30, 40, 50, 60, 70]
})

df

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name + '-name'

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
  
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# Add a slider(滑桿) to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# 設定左右欄位
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
