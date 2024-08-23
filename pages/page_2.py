import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='糖類產品')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹')
st.sidebar.page_link('pages/page_2.py', label='糖類')

# 標題
st.title('糖類')
