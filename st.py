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

# 加入自訂 CSS 和 JavaScript
st.markdown(
    """
    <style>
    .carousel-container {
        display: flex;
        align-items: center;
    }
    .carousel-wrapper {
        display: flex;
        overflow: hidden;
        width: 220px; /* 只顯示兩個按鈕的寬度 */
    }
    .carousel-buttons {
        display: flex;
        transition: transform 0.5s ease;
    }
    .carousel-button {
        flex: 0 0 100px; /* 每個按鈕的寬度 */
        margin: 5px;
        background-color: #cce7ff;
        color: #000;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    .nav-button {
        cursor: pointer;
        padding: 10px;
        background-color: #cce7ff;
        border-radius: 50%;
        margin: 0 10px;
    }
    </style>

    <div class="carousel-container">
        <div class="nav-button" onclick="moveCarousel(-1)">◀</div>
        <div class="carousel-wrapper">
            <div class="carousel-buttons" id="carousel">
                <div class="carousel-button">按鈕 1</div>
                <div class="carousel-button">按鈕 2</div>
                <div class="carousel-button">按鈕 3</div>
                <div class="carousel-button">按鈕 4</div>
            </div>
        </div>
        <div class="nav-button" onclick="moveCarousel(1)">▶</div>
    </div>

    <script>
    let currentIndex = 0;
    function moveCarousel(direction) {
        const carousel = document.getElementById("carousel");
        const buttons = document.querySelectorAll(".carousel-button");
        const totalButtons = buttons.length;
        currentIndex = (currentIndex + direction + totalButtons) % totalButtons;
        const offset = -currentIndex * 110; // 每個按鈕的寬度加上間距
        carousel.style.transform = `translateX(${offset}px)`;
    }
    </script>
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
