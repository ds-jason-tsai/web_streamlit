import os
import pandas as pd
import streamlit as st

prod_type = '醬油類'

# 瀏覽器頁籤
st.set_page_config(page_title=prod_type, layout="wide")

# 網頁標題
st.header(prod_type)

# sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹')
st.sidebar.page_link('pages/page_1.py',  label='糖類')
st.sidebar.page_link('pages/page_2.py',  label='麵粉類')
st.sidebar.page_link('pages/page_3.py',  label='粉類')
st.sidebar.page_link('pages/page_4.py',  label='油類')
st.sidebar.page_link('pages/page_5.py',  label='調味料')
st.sidebar.page_link('pages/page_6.py',  label='醬油類')
st.sidebar.page_link('pages/page_7.py',  label='罐頭類')
st.sidebar.page_link('pages/page_8.py',  label='農產品')
st.sidebar.page_link('pages/page_9.py',  label='海產類')
st.sidebar.page_link('pages/page_10.py', label='豆類')
st.sidebar.page_link('pages/page_11.py', label='中藥')
st.sidebar.page_link('pages/page_12.py', label='雜貨類')
st.sidebar.page_link('pages/page_13.py', label='冰用品')
st.sidebar.page_link('pages/page_14.py', label='茶咖啡')
st.sidebar.page_link('pages/page_15.py', label='王子麵')
st.sidebar.page_link('pages/page_16.py', label='泡麵類')
st.sidebar.page_link('pages/page_17.py', label='香辛料')

# 欄位排列
# left_column, right_column = st.columns(2)

# 製造間距
st.write(f"")
st.write(f"")
st.write(f"")

# 網頁子標題
st.write('產品細項')

df = pd.read_excel("../static/p6.xlsx")
st.dataframe(df, use_container_width=True)
