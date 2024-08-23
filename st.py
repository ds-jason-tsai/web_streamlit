import numpy as np
import pandas as pd
import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='啟元食品行', layout="wide")

# 網頁標題
st.header('首頁')

# Sidebar navigation
st.sidebar.page_link('st.py', label='公司介紹') 
st.sidebar.page_link('pages/page_2.py', label='糖類')

# image
# st.image('https://lh5.googleusercontent.com/p/AF1QipNF0A-hAXYtaPUHDXzESGzBftZsF7spDhSKmLas=s774-k-no')

# 加入自訂 CSS
st.markdown(
    """
    <style>
    .custom-link {
        display: block;
        padding: 10px;
        background-color: #cce7ff; /* 科技感淺藍色 */
        color: #fff; /* 白色文字 */
        text-align: center;
        text-decoration: none; /* 移除底線 */
        border-radius: 5px;
        margin: 5px 0;
        font-weight: normal; /* 去掉加粗 */
        transition: background-color 0.3s ease; /* 平滑過渡 */
    }
    .custom-link:hover {
        background-color: #99d0ff; /* 淺藍色 hover 效果 */
        color: #fff; /* 保持白色文字顏色 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 欄位排列 | 商品類選單
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)

with c1:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">糖類</a>', 
    unsafe_allow_html=True)
with c2:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">麵粉類</a>', 
    unsafe_allow_html=True)
with c3:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">粉類</a>', 
    unsafe_allow_html=True)
with c4:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">油類</a>', 
    unsafe_allow_html=True)
with c5:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">調味料</a>', 
    unsafe_allow_html=True)
with c6:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">醬油類</a>', 
    unsafe_allow_html=True)
with c7:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">罐頭類</a>', 
    unsafe_allow_html=True)
with c8:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">農產品</a>', 
    unsafe_allow_html=True)
with c9:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">海產類</a>', 
    unsafe_allow_html=True)

c10, c11, c12, c13, c14, c15, c16, c17, c18 = st.columns(9)

with c10:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">豆類</a>', 
    unsafe_allow_html=True)
with c11:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">中藥</a>', 
    unsafe_allow_html=True)
with c12:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">雜貨類</a>', 
    unsafe_allow_html=True)
with c13:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">冰用品</a>', 
    unsafe_allow_html=True)
with c14:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">茶咖啡</a>', 
    unsafe_allow_html=True)
with c15:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">王子麵</a>', 
    unsafe_allow_html=True)
with c16:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">泡麵類</a>', 
    unsafe_allow_html=True)
with c17:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">香辛料</a>', 
    unsafe_allow_html=True)

# 製造間距
st.write(f"")
st.write(f"")


# 欄位排列
left_column, right_column = st.columns(2)

# button widget
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
