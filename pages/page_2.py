import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='糖類')

# 網頁標題
st.header('糖類')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹') 
st.sidebar.page_link('pages/page_2.py', label='糖類')


# 欄位排列
left_column, right_column = st.columns(2)

with left_column:
    st.write('左側')

with right_column:
    st.write('右側')
