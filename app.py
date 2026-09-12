import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval 

st.set_page_config(page_title="Form Na Neko", page_icon="🦜", layout="wide")

FILE_NAME = "masu_aure.csv"
ADMIN_PASSWORD = "ALI@123" 

# ====== KARANTAR HOTUNA ======
@st.cache_data
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

logo = get_img_as_base64("logo.png") 
bg = get_img_as_base64("1734809626335.jpg")

# ====== CSS MAI RUBUTU MAI GIRMA ======
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');
    html, body, [class*="css"] {{font-family: 'Poppins', sans-serif;}}
    
    /* 1. BACKGROUND DIN PARROT */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 2. KATIN FARI MAI KARFI */
    .main-container {{
        max-width: 750px; 
        margin: 40px auto; 
        background: rgba(255, 255, 255, 0.98); 
        border-radius: 30px; 
        padding: 3rem; 
        box-shadow: 0 25px 60px rgba(0,0,0,0.5); 
        border: 5px solid #FFC107;
    }}
    
    /* 3. LOGO MAI GIRMA */
    .logo-container {{text-align: center; margin-bottom: 25px;}}
    .logo-container img {{
        border-radius: 30px; 
        border: 6px solid #FFC107; 
        width: 180px; /* Na kara girma */
        height: 180px; 
        object-fit: cover;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }}
    
    /* 4. RUBUTU MAI GIRMA SOSAI */
    .title {{
        text-align: center; 
        color: #0D47A1; 
        font-size: 45px; /* NA KARA GIRMA */
        font-weight: 900; 
        margin-bottom: 10px;
    }}
    .welcome {{
        text-align: center; 
        color: #000000; /* Baki mai duhu sosai */
        font-size: 22px; /* NA KARA GIRMA */
        margin-bottom: 35px;
        font-weight: 700;
    }}
    
    /* 5. INPUTS DA LABELS MAI GIRMA */
    label {{color: #0D47A1 !important; font-weight: 800 !important; font-size: 20px !important;}} /* LABEL */
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{
        border-radius: 15px; 
        border: 4px solid #0D47A1;
        background: white;
        color: black;
        font-weight: 800;
        font-size: 20px; /* NA KARA GIRMA */
        padding: 14px;
        height: 3.2em;
    }}
    
    .stRadio > div {{background: #FFF8E1; padding: 18px; border-radius: 15px; border: 3px solid #FFC107;}}
    .stRadio label {{font-size: 19px !important; font-weight: 700 !important;}} /* RADIO */
    
    /* 6. BUTTON MAI KATO SOSAI */
    .stButton>button {{
        background: linear-gradient(90deg, #FFC107 0%, #0D47A1 100%); 
        color: white; 
        border-radius: 20px; 
        height: 4.2em; 
        width: 100%; 
        font-size: 26px; /* NA KARA GIRMA */
        font-weight: 900; 
        border: none;
        margin-top: 20px;
        letter-spacing: 1px;
    }}
    .stButton>button:hover {{transform: scale(1.05); transition: 0.3s;}}
    
    /* NA SAKE GIRMA SUCCESS/ERROR MESSAGES */
    .stAlert {{font-size: 18px !important; font-weight: 700 !important;}}
    
    @media (max-width: 750px) {{
        .main-container {{padding: 1.8rem; margin: 15px;}}
        .title {{font-size: 34px;}}
        .welcome {{font-size: 18px;}}
        .logo-container img {{width: 130px; height: 130px;}}
    }}
    </style>
""", unsafe_allow_html=True)

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

if menu == "Form Na Register":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    if logo:
        st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo}"></div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Logo bai samu ba. Ka tabbatar sunan fayil din daidai ne: `logo.png`")
        
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
                if shekaru >= 18: st.info(f"An karbe ka! Ka girma kakai Aure ✅")
                else: st.warning(f"Baka kai Aureba. Kajira shekara {18 - shekaru} tukunnan ❌")
                if shekaru >= 35: st.error("Kai ka wuce Aure. Ka yi girma sosai 😂")
                st.balloons()
            else: st.error("Taf, da fatan ka cika dukkan bayanai")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Shafin Admin 🔒":
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
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Sauke Data", df.to_csv(index=False).encode('utf-8'), "masu_aure.csv", "text/csv")
        else: st.info("Babu wanda ya yi register tukuna")
    elif password: st.error("Password ba daidai ba ne ❌")
    st.markdown('</div>', unsafe_allow_html=True)
