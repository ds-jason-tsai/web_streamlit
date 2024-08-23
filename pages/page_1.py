import pandas as pd
import streamlit as st

prod_type = '糖類'

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
left_column, right_column = st.columns(2)

with left_column:
    st.header('圖片')
    st.write('左側')

with right_column:
    st.header('介紹')
    st.write('商品明細')
    
    data = {
        "貨品編號": [
        "1101005", "1102004",  "1102005",  "1102007",  "1102009", "1103010", "1105100", 
        "1106100", "1107600",  "1107721",  "1107723",  "1108401", "1108503", "1108510", 
        "1109000", "1109103",  "1109106",  "1109112",  "1109206", "1109320", "1109321", 
        "1109337", "1109404",  "1109501",  "1109503",  "1109520", "1109546", "1109547", 
        "1109548", "11093311", "11093391", "11095451", "3110302", "3110306"
    ],
    "貨品名稱": [
        "(本)特砂50KG", "(進)二砂50KG", "(本地)二砂50KG", "台糖二砂1K-20入", "進口二砂25kg", 
        "(台糖)細砂 1KG-20包", "寶山黑糖30KG", "寶山黑糖450G-20入", "正港冰糖(細)-30KG", 
        "志濱(細)冰糖-30K", "志濱(小)冰糖-30K", "紅桃牌*冰糖500G-50入", "＜紅冰糖>3K-10包入", 
        "東承<紅>冰糖450g-20小", "冬瓜條3KG-10入(達益)", "(三元)冬瓜角540g10塊-3袋", 
        "老頭家冬瓜茶磚550g-30入", "達益冬瓜角-60斤入", "桔餅3斤-30包(德合記)", "麥芽糖鐵桶(紅色24KG)", 
        "麥芽糖鐵桶(白色24KG)", "水***麥芽糖  24K", "粉糖-18KG", "豐年果糖25KG", "豐年果糖5L-3入", 
        "豐年-果糖1.5KG-6入", "骰子棉花糖1K-5入", "白色迷你棉花糖1K-5包入", "白棉花糖(小)1k-5入", 
        "富鼎盛-水麥芽5kg-4入", "富鼎盛-水麥芽1.2k-8入", "棉花糖(白)大顆1K-5入", 
        "日本上白糖-1kg-10入", "日本三溫糖-1kg10入"
    ],
    "單位": [
        "件", "件", "件", "件", "件", "件", "箱", "件", "箱", "箱", "箱", "箱", "箱", 
        "箱", "箱", "箱", "箱", "箱", "箱", "件", "件", "件", "件", "件", "箱", 
        "箱", "箱", "箱", "箱", "箱", "箱", "箱", "箱", "箱"
    ]
    }

    df = pd.DataFrame(data)
