import numpy as np
import pandas as pd
import streamlit as st

# 瀏覽器頁籤
st.set_page_config(page_title='啟元食品行', layout="wide")

# 網頁標題
st.header('首頁')

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

# image
# st.image('https://lh5.googleusercontent.com/p/AF1QipNF0A-hAXYtaPUHDXzESGzBftZsF7spDhSKmLas=s774-k-no')

# 加入自訂 CSS
st.markdown(
    """
    <style>
    .custom-link {
        display: block;
        padding: 10px;
        background-color: #cce7ff; /* 淺藍色 */
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
    st.markdown('<a class="custom-link" href="/page_1" target="_self">糖類</a>', 
    unsafe_allow_html=True)
with c2:
    st.markdown('<a class="custom-link" href="/page_2" target="_self">麵粉類</a>', 
    unsafe_allow_html=True)
with c3:
    st.markdown('<a class="custom-link" href="/page_3" target="_self">粉類</a>', 
    unsafe_allow_html=True)
with c4:
    st.markdown('<a class="custom-link" href="/page_4" target="_self">油類</a>', 
    unsafe_allow_html=True)
with c5:
    st.markdown('<a class="custom-link" href="/page_5" target="_self">調味料</a>', 
    unsafe_allow_html=True)
with c6:
    st.markdown('<a class="custom-link" href="/page_6" target="_self">醬油類</a>', 
    unsafe_allow_html=True)
with c7:
    st.markdown('<a class="custom-link" href="/page_7" target="_self">罐頭類</a>', 
    unsafe_allow_html=True)
with c8:
    st.markdown('<a class="custom-link" href="/page_8" target="_self">農產品</a>', 
    unsafe_allow_html=True)
with c9:
    st.markdown('<a class="custom-link" href="/page_9" target="_self">海產類</a>', 
    unsafe_allow_html=True)

c10, c11, c12, c13, c14, c15, c16, c17, c18 = st.columns(9)

with c10:
    st.markdown('<a class="custom-link" href="/page_10" target="_self">豆類</a>', 
    unsafe_allow_html=True)
with c11:
    st.markdown('<a class="custom-link" href="/page_11" target="_self">中藥</a>', 
    unsafe_allow_html=True)
with c12:
    st.markdown('<a class="custom-link" href="/page_12" target="_self">雜貨類</a>', 
    unsafe_allow_html=True)
with c13:
    st.markdown('<a class="custom-link" href="/page_13" target="_self">冰用品</a>', 
    unsafe_allow_html=True)
with c14:
    st.markdown('<a class="custom-link" href="/page_14" target="_self">茶咖啡</a>', 
    unsafe_allow_html=True)
with c15:
    st.markdown('<a class="custom-link" href="/page_15" target="_self">王子麵</a>', 
    unsafe_allow_html=True)
with c16:
    st.markdown('<a class="custom-link" href="/page_16" target="_self">泡麵類</a>', 
    unsafe_allow_html=True)
with c17:
    st.markdown('<a class="custom-link" href="/page_17" target="_self">香辛料</a>', 
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
