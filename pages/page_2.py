import streamlit as st

# 頁籤名稱
st.header('糖類')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹')
st.sidebar.page_link('pages/page_2.py', label='糖類')
