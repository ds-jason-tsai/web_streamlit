import numpy as np
import pandas as pd
import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='啟元食品行')

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
        color: #000; /* 文字顏色 */
        text-align: center;
        text-decoration: none; /* 移除底線 */
        border-radius: 5px;
        margin: 5px 0;
        font-weight: bold; /* 字體加粗 */
        transition: background-color 0.3s ease; /* 平滑過渡 */
    }
    .custom-link:hover {
        background-color: #99d0ff; /* 淺藍色 hover 效果 */
        color: #000; /* 保持文字顏色 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 欄位排列 | 商品類選單
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">分頁連結</a>', 
    unsafe_allow_html=True)
with c2:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">分頁連結</a>', 
    unsafe_allow_html=True)
with c3:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">分頁連結</a>', 
    unsafe_allow_html=True)
with c4:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">分頁連結</a>', 
    unsafe_allow_html=True)


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
