import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval 

st.set_page_config(page_title="Form Na Neko", page_icon="🦜", layout="wide")

FILE_NAME = "masu_aure.csv"
ADMIN_PASSWORD = "ALI@123" 

# ====== SAITA LOGO NA PARROT ======
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("wa_image_6507695863678731215") 

# ====== CSS MAI GIRMA SOSAI - DUK RUBUTU BAKI ======
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap');
    html, body, [class*="css"] {{font-family: 'Poppins', sans-serif; color: #000 !important;}} /* DUK RUBUTU BAKI */
    
    .main {{background: linear-gradient(135deg, #0a0f1e 0%, #1a237e 100%); padding: 2rem;}}
    .stApp {{max-width: 700px; margin: auto; background: white; border-radius: 25px; padding: 2.5rem; box-shadow: 0 15px 40px rgba(255,193,7,0.3); border: 4px solid #FFC107;}}
    
    .logo-container {{text-align: center; margin-bottom: 20px;}}
    .logo-container img {{border-radius: 50%; border: 5px solid #FFC107; width: 140px; height: 140px; object-fit: cover;}}
    
    /* DUKKAN KANUNAN RUBUTU SUN ZAMA GIRMA DA BAKI */
    .title {{text-align: center; color: #000000; font-size: 42px; font-weight: 900; margin-bottom: 10px;}}
    .welcome {{text-align: center; color: #000000; font-size: 22px; font-weight: 600; margin-bottom: 30px;}}
    h3 {{color: #000000 !important; font-size: 28px !important; font-weight: 700 !important;}}
    label {{color: #000 !important; font-size: 20px !important; font-weight: 700 !important;}}
    
    /* INPUTS SUNYI GIRMA */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{border-radius: 12px; border: 3px solid #000000; font-size: 20px !important; color: #000000 !important; padding: 12px;}}
    .stRadio > div {{background: linear-gradient(90deg, #FFF8E1 0%, #E3F2FD 100%); padding: 15px; border-radius: 12px; border: 2px solid #000;}}
    .stRadio label {{font-size: 20px !important; font-weight: 700 !important; color: #000000 !important;}}
    
    /* BUTTON MAI GIRMA */
    .stButton>button {{background: linear-gradient(90deg, #FFC107 0%, #1a237e 100%); color: white !important; border-radius: 18px; height: 4em; width: 100%; font-size: 24px !important; font-weight: 900; border: none;}}
    .stButton>button:hover {{transform: scale(1.03); transition: 0.3s;}}
    
    /* SAKAMAKO MAI GIRMA SOSAI */
    .result-box {{
        font-size: 32px !important; 
        font-weight: 900 !important; 
        text-align: center; 
        padding: 25px; 
        border-radius: 20px; 
        margin-top: 20px;
        color: #000 !important;
    }}
    .success-result {{background-color: #C8E6C9; border: 3px solid #2E7D32;}}
    .warning-result {{background-color: #FFF9C4; border: 3px solid #F9A825;}}
    .error-result {{background-color: #FFCDD2; border: 3px solid #C62828;}}
    
    /* ADMIN */
    [data-testid="stMetricValue"] {{font-size: 40px !important; color: #000 !important;}}
    [data-testid="stMetricLabel"] {{font-size: 18px !important; color: #000 !important;}}
    
    @media (max-width: 700px) {{
        .stApp {{padding: 1.5rem; margin: 10px;}}
        .title {{font-size: 34px;}}
        .welcome {{font-size: 18px;}}
        label {{font-size: 18px !important;}}
        .result-box {{font-size: 26px !important;}}
    }}
    </style>
""", unsafe_allow_html=True)

# Aiki na daukar bayanai
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

device_info = streamlit_js_eval(js_expressions='navigator.userAgent', key='ua')

menu = st.sidebar.radio("📋 Menu", ["Form Na Register", "Shafin Admin 🔒"])

# ====== SHAGI 1: NA JAMA'A ======
if menu == "Form Na Register":
    st.markdown(f'<div class="logo-container"><img src="data:image/jpeg;base64,{img}"></div>', unsafe_allow_html=True)
    st.markdown('<p class="title">🦜 FORM NA MASU AURE</p>', unsafe_allow_html=True)
    st.markdown('<p class="welcome">BARKA DA ZUWA! CIKA BAYANANKA DOMIN DUBA CANCANTARKA</p>', unsafe_allow_html=True)

    with st.form("register_form", clear_on_submit=True):
        suna = st.text_input("1. MEYE SUNANKA?")
        shekaru = st.number_input("2. SHEKARUNKA NAWA?", min_value=1, max_value=100, step=1)
        jinsi = st.radio("3. KAI NAMIJI NE KO MACE?", ["NAMIJI", "MACE"], horizontal=True)
        submitted = st.form_submit_button("AIKA FORM 🚀")

        if submitted:
            if suna and shekaru:
                lokaci = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_user(suna, jinsi, shekaru, lokaci, device_info)
                
                # SAKAMAKO MAI GIRMA SOSAI
                if shekaru >= 18 and shekaru < 35:
                    st.markdown(f'<div class="result-box success-result">✅ BARKA {suna.upper()}! <br> AN KARBE KA! KAI GIRMACE KAKAI AURE</div>', unsafe_allow_html=True)
                elif shekaru < 18:
                    shekaru_dazuwa = 18 - shekaru
                    st.markdown(f'<div class="result-box warning-result">❌ HABA {suna.upper()}! <br> BAKA KAI AUREBA. <br> KAJIRA SHEKARA {shekaru_dazuwa} TUKUNAN</div>', unsafe_allow_html=True)
                elif shekaru >= 35:
                    st.markdown(f'<div class="result-box error-result">😂 HABA {suna.upper()}! <br> KAI KA WUCE AURE! <br> KA YI GIRMA SOSAI</div>', unsafe_allow_html=True)
                
                st.balloons()
            else:
                st.markdown(f'<div class="result-box error-result">⚠️ TAF! DA FATAN KA CIKA DUKKAN BAYANAI</div>', unsafe_allow_html=True)

# ====== SHAGI 2: NA ADMIN ======
elif menu == "Shafin Admin 🔒":
    st.markdown('<p class="title">🔐 SHAFIN ADMIN</p>', unsafe_allow_html=True)
    password = st.text_input("SHIGAR DA PASSWORD NA ADMIN", type="password")

    if password == ADMIN_PASSWORD:
        df = load_users()
        if not df.empty:
            st.success("BARKA DA ZUWA ADMIN!", icon="👑")
            
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("JIMILLA", len(df))
            with col2: st.metric("MAZAJE", len(df[df["Jinsi"] == "NAMIJI"]))
            with col3: st.metric("MATA", len(df[df["Jinsi"] == "MACE"]))
            
            st.write("### JERIN DUK WANDA YA YI REGISTER")
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 SAUKE DATA A MATSAYIN CSV", df.to_csv(index=False).encode('utf-8'), "masu_aure.csv", "text/csv")
        else:
            st.info("BABU WANDA YA YI REGISTER TUKUNA")
    elif password:
        st.error("PASSWORD BA DAIDAI BA NE ❌")
