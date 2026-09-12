import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval 

st.set_page_config(page_title="Form Na Neko", page_icon="🦜", layout="wide")

FILE_NAME = "masu_aure.csv"
ADMIN_PASSWORD = "ALI@123" 

# ====== SAITA LOGO DA BACKGROUND ======
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 1. Wannan shine logo din ka
logo = get_img_as_base64("logo.png") 
# 2. Wannan shine background mai lambobi
bg = get_img_as_base64("1734809626335.jpg")

# ====== CSS MAI KYAU DA BACKGROUND ======
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] {{font-family: 'Poppins', sans-serif;}}
    
    /* Anan muka sanya background din mai lambobi */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Wannan shine katin fari da ke dauke da form */
    .main-container {{
        max-width: 650px; 
        margin: 40px auto; 
        background: rgba(255, 255, 255, 0.95); 
        border-radius: 25px; 
        padding: 2rem; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.3); 
        border: 3px solid #FFC107;
        backdrop-filter: blur(5px);
    }}
    
    .logo-container {{text-align: center; margin-bottom: 15px;}}
    .logo-container img {{border-radius: 20px; border: 4px solid #FFC107; width: 140px; height: 140px; object-fit: cover;}}
    
    .title {{text-align: center; color: #1a237e; font-size: 34px; font-weight: 700; margin-bottom: 5px;}}
    .welcome {{text-align: center; color: #555; font-size: 16px; margin-bottom: 25px;}}
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{border-radius: 12px; border: 2px solid #1a237e;}}
    .stRadio > div {{background: linear-gradient(90deg, #FFF8E1 0%, #E3F2FD 100%); padding: 12px; border-radius: 12px; border: 1px solid #FFC107;}}
    
    .stButton>button {{background: linear-gradient(90deg, #FFC107 0%, #1a237e 100%); color: white; border-radius: 15px; height: 3.5em; width: 100%; font-size: 18px; font-weight: 700; border: none;}}
    .stButton>button:hover {{transform: scale(1.03); transition: 0.3s; box-shadow: 0 5px 15px rgba(255,193,7,0.4);}}
    
    /* Don waya */
    @media (max-width: 650px) {{
        .main-container {{padding: 1.2rem; margin: 10px;}}
        .title {{font-size: 28px;}}
        .logo-container img {{width: 100px; height: 100px;}}
    }}
    </style>
""", unsafe_allow_html=True)

# Aiki na adana bayanai
def save_user(suna, jinsi, shekaru, lokaci, device_info):
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Suna", "Jinsi", "Shekaru", "Lokacin Register", "Device/Browser"])
    else:
        df = pd.read_csv(FILE_NAME)
    new_data = pd.DataFrame([[suna, jinsi, shekaru, lokaci, device_info]], columns=["Suna", "Jinsi", "Shekaru", "Lokacin Register", "Device/Browser"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

def load_users():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Suna", "Jinsi", "Shekaru", "Lokacin Register", "Device/Browser"])

# Daukar bayanai na waya/browser
device_info = streamlit_js_eval(js_expressions='navigator.userAgent', key='ua')

# ====== MENU NA SAMA ======
menu = st.sidebar.radio("📋 Menu", ["Form Na Register", "Shafin Admin 🔒"])

# ====== SHAGI 1: NA JAMA'A ======
if menu == "Form Na Register":
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        # Anan muka saka logo.png
        st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo}"></div>', unsafe_allow_html=True)
        st.markdown('<p class="title">🦜 Form Na Masu Aure</p>', unsafe_allow_html=True)
        st.markdown('<p class="welcome">Barka da zuwa! Cika bayanan ka domin duba cancantarka 😼</p>', unsafe_allow_html=True)

        with st.form("register_form", clear_on_submit=True):
            suna = st.text_input("1. Meye sunanka?")
            shekaru = st.number_input("2. Shekarunka nawa?", min_value=1, max_value=100, step=1)
            jinsi = st.radio("3. Kai NAMIJI ne ko MACE?", ["NAMIJI", "MACE"], horizontal=True)
            submitted = st.form_submit_button("Aika Form 🚀")

            if submitted:
                if suna and shekaru:
                    lokaci = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_user(suna, jinsi, shekaru, lokaci, device_info)
                    
                    st.success(f"Barka da zuwa {suna}!", icon="✅")
                    if shekaru >= 18:
                        st.info(f"An karbe ka! Ka girma kakai Aure ✅")
                    else:
                        shekaru_dazuwa = 18 - shekaru
                        st.warning(f"Baka kai Aureba. Kajira kakaikai shekara {shekaru_dazuwa} tukunnan ❌")
                    if shekaru >= 35:
                        st.error("Kai ka wuce Aure. Ka yi girma sosai 😂")
                    st.balloons()
                else:
                    st.error("Taf, da fatan ka cika dukkan bayanai")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ====== SHAGI 2: NA ADMIN ======
elif menu == "Shafin Admin 🔒":
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.markdown('<p class="title">🔐 Shafin Admin</p>', unsafe_allow_html=True)
        password = st.text_input("Shigar da password na admin", type="password")

        if password == ADMIN_PASSWORD:
            df = load_users()
            if not df.empty:
                st.success("Barka da zuwa Admin!", icon="👑")
                
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Jimilla", len(df))
                with col2: st.metric("Mazaje", len(df[df["Jinsi"] == "NAMIJI"]))
                with col3: st.metric("Mata", len(df[df["Jinsi"] == "MACE"]))
                
                st.write("### Jerin Duk Wanda Ya Yi Register")
                st.dataframe(df, use_container_width=True)
                st.download_button("📥 Sauke Data a matsayin CSV", df.to_csv(index=False).encode('utf-8'), "masu_aure.csv", "text/csv")
            else:
                st.info("Babu wanda ya yi register tukuna")
        elif password:
            st.error("Password ba daidai ba ne ❌")
        st.markdown('</div>', unsafe_allow_html=True)
