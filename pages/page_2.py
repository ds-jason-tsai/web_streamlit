import streamlit as st

# 頁籤名稱
st.header('P2')

# Sidebar navigation
st.sidebar.page_link('st.py', label='Home')
st.sidebar.page_link('pages/page_2.py', label='P2')

st.title(f'🛡️ Competition Checker')

