import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='糖類')

# 頁籤名稱
st.header('糖類')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹') 
st.sidebar.page_link('pages/page_2.py', label='糖類')
