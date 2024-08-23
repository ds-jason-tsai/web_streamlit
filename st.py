import numpy as np
import pandas as pd
import streamlit as st
# from streamlit_navigation_bar import st_navbar

# page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
# st.write(page)

# 瀏覽器頁籤與其他設定
st.set_page_config(page_title='啟元食品行', layout="wide")

# 網頁標題
st.header('啟元食品行')

# 製造間距
st.write(f"")
st.write(f"")

st.image("https://lh5.googleusercontent.com/p/AF1QipNF0A-hAXYtaPUHDXzESGzBftZsF7spDhSKmLas=s774-k-no")

st.write(f"")
st.write(f"")

st.subheader('關於我們')
st.write("啓懋食品行為南北雜貨、烘焙食材，餐廳飯店食品材供應商我們重視每一位員工")
st.write("除了有良好工作環境、也提供學習及成長的空間，歡迎優秀的朋友一起加入啓懋食品行的工作行列。")

st.write(f"")
st.write(f"")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://lh5.googleusercontent.com/p/AF1QipMsRbfascvOIbfRSoaEKPJhZOwx9opM_VJSJlJe=s580-k-no")
with col2:
    st.image("https://lh5.googleusercontent.com/p/AF1QipNCkFdy2ZrVG-om_jCjUGdSR_mZ-PGkbIez3pMc=s676-k-no")
with col3:
    st.image("https://lh5.googleusercontent.com/p/AF1QipP7dRq4g-IePOLlcgec--g5QRpL87RewIdH2vxr=s676-k-no")

st.write(f"")
st.write(f"")

# 網頁標題
st.subheader('產品分類')
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

# Include Font Awesome CDN(for icon)
st.markdown(
    """
    <link rel  = "stylesheet" 
          href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    >
    """,
    unsafe_allow_html=True
)

# 加入自訂 CSS
st.markdown(
    """
    <style>
    .custom-link {
        display: block;
        padding: 10px;
        /* 淺藍色 */
        background-color: #cce7ff;
        /* 白色字 */
        color: #fff; 
        text-align: center;
        /* 無底線 */
        text-decoration: none;
        border-radius: 5px;
        margin: 5px 0;
        /* 無加粗 */
        font-weight: normal;
        /* 平滑過渡 */
        transition: background-color 0.3s ease;
    }
    .custom-link:hover {
        /* 淺藍色 hover 效果 */
        background-color: #99d0ff;
        /* 保持白色文字顏色 */
        color: #fff;
    }
    .custom-link i {
        /* Add space between icon and text */
        margin-right: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 欄位排列 | 商品類選單
c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

with c1:
    st.markdown('<a class="custom-link" href="/page_1" target="_self"> \
                 <i class="fas fa-cube"></i> 糖類</a>', 
                 unsafe_allow_html=True)
with c2:
    st.markdown('<a class="custom-link" href="/page_2" target="_self"> \
                 <i class="fas fa-bread-slice"></i> 麵粉類</a>', 
                 unsafe_allow_html=True)
with c3:
    st.markdown('<a class="custom-link" href="/page_3" target="_self"> \
                 <i class="fas fa-boxes"></i> 粉類</a>', 
                 unsafe_allow_html=True)
with c4:
    st.markdown('<a class="custom-link" href="/page_4" target="_self"> \
                 <i class="fas fa-oil-can"></i> 油類</a>', 
                 unsafe_allow_html=True)
with c5:
    st.markdown('<a class="custom-link" href="/page_5" target="_self"> \
                 <i class="fas fa-mortar-pestle"></i> 調味料</a>', 
                 unsafe_allow_html=True)
with c6:
    st.markdown('<a class="custom-link" href="/page_6" target="_self"> \
                 <i class="fas fa-prescription-bottle-alt"></i> 醬油類</a>', 
                 unsafe_allow_html=True)
with c7:
    st.markdown('<a class="custom-link" href="/page_7" target="_self"> \
                 <i class="fas fa-spray-can"></i> 罐頭類</a>', 
                 unsafe_allow_html=True)

c8, c9, c10, c11, c12, c13, c14 = st.columns(7)

with c8:
    st.markdown('<a class="custom-link" href="/page_8" target="_self"> \
                 <i class="fas fa-carrot"></i> 農產品</a>', 
                 unsafe_allow_html=True)
with c9:
    st.markdown('<a class="custom-link" href="/page_9" target="_self"> \
                 <i class="fas fa-fish"></i> 海產類</a>', 
                 unsafe_allow_html=True)
with c10:
    st.markdown('<a class="custom-link" href="/page_10" target="_self"> \
                 <i class="fas fa-seedling"></i> 豆類</a>', 
                 unsafe_allow_html=True)
with c11:
    st.markdown('<a class="custom-link" href="/page_11" target="_self"> \
                 <i class="fas fa-leaf"></i> 中藥</a>', 
                 unsafe_allow_html=True)
with c12:
    st.markdown('<a class="custom-link" href="/page_12" target="_self"> \
                 <i class="fas fa-box-open"></i> 雜貨類</a>', 
                 unsafe_allow_html=True)
with c13:
    st.markdown('<a class="custom-link" href="/page_13" target="_self"> \
                 <i class="fas fa-ice-cream"></i> 冰用品</a>', 
                 unsafe_allow_html=True)

c15, c16, c17, c18 , c19 , c20 , c21 = st.columns(7)
with c14:
    st.markdown('<a class="custom-link" href="/page_14" target="_self"> \
                 <i class="fas fa-coffee"></i> 茶咖啡</a>', 
                 unsafe_allow_html=True)
with c15:
    st.markdown('<a class="custom-link" href="/page_15" target="_self"> \
                 <i class="fas fa-drumstick-bite"></i> 王子麵</a>', 
                 unsafe_allow_html=True)
with c16:
    st.markdown('<a class="custom-link" href="/page_16" target="_self"> \
                 <i class="fas fa-utensil-spoon"></i> 泡麵類</a>', 
                 unsafe_allow_html=True)
with c17:
    st.markdown('<a class="custom-link" href="/page_17" target="_self"> \
                 <i class="fas fa-pepper-hot"></i> 香辛料</a>', 
                 unsafe_allow_html=True)


# 製造間距
st.write(f"")
st.write(f"")
st.write(f"")
st.write(f"")
st.write(f"")
st.write(f"")

# 網頁標題
st.subheader('客戶怎麼說？', divider='gray')
col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"")
    st.subheader("客戶一")
    st.write("初到宜蘭尋找烘焙材料行，結果發現這間賣南北貨食材，一問才知旁邊另外裝潢一間專賣烘焙材料用品，光麵粉和糖選擇很多，模具也很多，要用的大部份都找得到，逛起來舒適，老闆有問必答，態度好很用心，有需要的人可以來這買。")
with col2:
    st.write(f"")
    st.subheader("客戶二")
    st.write("是一間很優質的食品材料行，東西齊全價格合理，旁邊的烘焙材料行物品也很齊全，很多種類可以選擇。但有個小小的請求，因為不是住在宜蘭市區，通常都只有假日才能前往，之前星期六都有營業，現在六日都休息，變得沒有辦法去購買，好困擾，希望能營業星期六的某一個時段，像是早上、中午或者下午")
with col3:
    st.write(f"")
    st.subheader("客戶三")
    st.write("停車方便，南北雜貨醬料一應俱全，價格都是最實惠的，最喜歡去的是烘培部，空間大擺放整齊，材料齊全經常有新品，補貨時還可以順便逛逛，令人一再回顧的好地方，有出貨給其他廠商，工作人員經常都是在理貨的狀態，有需要可以叫他們一下以免久等")

st.write(f"")
st.write(f"")
st.write(f"")
st.write(f"")

# 網頁標題
st.subheader('聯絡我們', divider='gray')
st.write(f"市話: 03-9309578")
st.write(f"地址: (260)宜蘭縣宜蘭市七張路333號")

