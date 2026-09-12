import streamlit as st
import pandas as pd
import os
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval # Wannan shine zai dauko bayanan waya

st.set_page_config(page_title="Form Na Neko", page_icon="💍", layout="wide") # wide yana kyautatawa a waya

FILE_NAME = "masu_aure.csv"
ADMIN_PASSWORD = "ALI@123" 

# ====== CSS MAI KYAU NA GASKIYA - RESPONSIVE ======
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] {font-family: 'Poppins', sans-serif;}
    
    .main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem;}
    .stApp {max-width: 600px; margin: auto; background: white; border-radius: 20px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2);}
    
    .title {text-align: center; color: #764ba2; font-size: 32px; font-weight: 700; margin-bottom: 10px;}
    .welcome {text-align: center; color: #555; font-size: 16px; margin-bottom: 30px;}
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input {border-radius: 10px; border: 2px solid #ddd;}
    .stRadio > div {background-color: #f0f2f6; padding: 10px; border-radius: 10px;}
    
    .stButton>button {background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 12px; height: 3.2em; width: 100%; font-size: 18px; font-weight: 600; border: none;}
    .stButton>button:hover {transform: scale(1.02); transition: 0.2s;}
    
    /* Don waya */
    @media (max-width: 600px) {
        .stApp {padding: 1rem; margin: 10px;}
        .title {font-size: 26px;}
    }
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

# Daukar bayanai na waya/browser
device_info = streamlit_js_eval(js_expressions='navigator.userAgent', key='ua')

# ====== MENU NA SAMA ======
menu = st.sidebar.radio("Menu", ["Form Na Register", "Shafin Admin 🔒"])

# ====== SHAGI 1: NA JAMA'A ======
if menu == "Form Na Register":
    st.markdown('<p class="title">📝 Form Na Masu Aure</p>', unsafe_allow_html=True)
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
                
                st.success(f"Barka da zuwa {suna}!")
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

# ====== SHAGI 2: NA ADMIN ======
elif menu == "Shafin Admin 🔒":
    st.markdown('<p class="title">🔐 Shafin Admin</p>', unsafe_allow_html=True)
    password = st.text_input("Shigar da password na admin", type="password")

    if password == ADMIN_PASSWORD:
        df = load_users()
        if not df.empty:
            st.success("Barka da zuwa Admin!")
            
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Jimilla", len(df))
            with col2: st.metric("Mazaje", len(df[df["Jinsi"] == "NAMIJI"]))
            with col3: st.metric("Mata", len(df[df["Jinsi"] == "MACE"]))
            
            st.write("### Jerin Duk Wanda Ya Yi Register")
            st.dataframe(df, use_container_width=True)
            st.download_button("Sauke Data a matsayin CSV", df.to_csv(index=False).encode('utf-8'), "masu_aure.csv", "text/csv")
        else:
            st.info("Babu wanda ya yi register tukuna")
    elif password:
        st.error("Password ba daidai ba ne ❌")