import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval 

st.set_page_config(page_title="Form Na Ali Umar", page_icon="🖥️", layout="wide")

FILE_NAME = "masu_aure.csv"
ADMIN_PASSWORD = "ALI@123" 

# ====== KARANTAR WALFA ======
@st.cache_data
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

bg = get_img_as_base64("longo.jpg") 

# ====== CSS MAI RUBUTU MAI JA MAI GIRMA ======
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');
    html, body, [class*="css"] {{font-family: 'Poppins', sans-serif;}}
    
    /* 1. WALFA TA WEBSITE */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 2. KATIN FARI MAI DUHU SOSAI DON JA YA FITO */
    .main-container {{
        max-width: 900px; 
        margin: 40px auto; 
        background: rgba(0, 0, 0, 0.7); /* BAKI MAI DUHU 70% */
        border-radius: 30px; 
        padding: 3.5rem; 
        box-shadow: 0 25px 60px rgba(255,0,0,0.4); 
        border: 5px solid #FF0000; /* JA BORDER */
    }}
    
    /* 3. TITLE MAI JA MAI GIRMA */
    .title {{
        text-align: center; 
        color: #FF0000; /* JA */
        font-size: 55px; /* MAI GIRMA SOSAI */
        font-weight: 900; 
        margin-bottom: 20px;
        text-transform: uppercase;
        text-shadow: 3px 3px 6px black; /* INUWA DON YA FITO */
    }}
    
    /* 4. WELCOME MAI JA MAI KATO SOSAI */
    .welcome {{
        text-align: center; 
        color: #FF0000; /* JA */
        font-size: 26px; /* NA KARA GIRMA SOSAI */
        margin-bottom: 40px;
        font-weight: 900; /* BOLD SOSAI */
        line-height: 2.2; /* SARARI MAI YAWA */
        white-space: pre-line; 
        text-transform: uppercase;
        text-shadow: 2px 2px 4px black; /* INUWA DON YA FITO AKAN WALFA */
        letter-spacing: 1px;
    }}
    
    /* 5. INPUTS DA LABELS MAI JA */
    label {{color: #FF0000 !important; font-weight: 900 !important; font-size: 24px !important; text-transform: uppercase; text-shadow: 1px 1px 2px black;}}
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input {{
        border-radius: 15px; 
        border: 5px solid #FF0000;
        background: rgba(255,255,255,0.95);
        color: black;
        font-weight: 900;
        font-size: 24px; 
        padding: 18px;
        height: 3.8em;
        text-transform: capitalize;
    }}
    
    .stRadio > div {{background: rgba(255,255,255,0.95); padding: 22px; border-radius: 15px; border: 4px solid #FF0000;}}
    .stRadio label {{font-size: 22px !important; font-weight: 900 !important; text-transform: uppercase; color: #0D47A1 !important;}}
    
    /* 6. BUTTON MAI JA MAI KATO */
    .stButton>button {{
        background: linear-gradient(90deg, #FF0000 0%, #8B0000 100%); /* JA ZUWA DUHUN JA */
        color: white; 
        border-radius: 20px; 
        height: 4.8em; 
        width: 100%; 
        font-size: 32px; /* MAI GIRMA SOSAI */
        font-weight: 900; 
        border: none;
        margin-top: 30px;
        letter-spacing: 3px;
        text-transform: uppercase;
        box-shadow: 0 8px 20px rgba(255,0,0,0.5);
    }}
    .stButton>button:hover {{transform: scale(1.08); transition: 0.3s;}}
    
    .stAlert {{font-size: 22px !important; font-weight: 900 !important; text-transform: uppercase;}}
    
    @media (max-width: 900px) {{
        .main-container {{padding: 2rem; margin: 15px;}}
        .title {{font-size: 38px;}}
        .welcome {{font-size: 20px;}}
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
menu = st.sidebar.radio("📋 MENU", ["FORM NA REGISTER", "SHAFIN ADMIN 🔒"])

if menu == "FORM NA REGISTER":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
    st.markdown('<p class="title">🖥️ FORM NA ALI UMAR</p>', unsafe_allow_html=True)
    
    welcome_text = """INA MAIYI MUKU BARKA DA ZIYARTAR SHAFINA SUNANA ALI UMAR MUHAMMAD NI DALIBIN CYBER SECURITY NE WANNAN WEBSITE DIN NA KIR KIRESHINE DOMIN TEST DAKUMA GWAJE GWAJE NA HARKAR PYTHON PROGRAMMING 

ZAKU IYA CIKA SUNANKU DA SHEKARUNKU WANNAN WEBSITE DIN INDAI KAFADA MASA 
SHEKARUNKA DAIDAI ZAIFADA MAKA KA KAI KAYI AURE NE KO BAKA KAIBA🙄

🤣😄😂 WANNAN SHINE LOKACIN FARKO DANA FARA KIR KIRAN ABU 

🖥️🖥️🖥️🙏 INA MAI YIMUKU GODIYA DA ZIYARTAR SHAFINA🫣

🙏NAGODE"""
    
    st.markdown(f'<p class="welcome">{welcome_text}</p>', unsafe_allow_html=True)

    with st.form("register_form", clear_on_submit=True):
        suna = st.text_input("1. MEYE SUNANKA?")
        shekaru = st.number_input("2. SHEKARUNKA NAWA?", min_value=1, max_value=100, step=1)
        jinsi = st.radio("3. KAI NAMIJI NE KO MACE?", ["NAMIJI", "MACE"], horizontal=True)
        submitted = st.form_submit_button("AIKA FORM 🚀")

        if submitted:
            if suna and shekaru:
                lokaci = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_user(suna, jinsi, shekaru, lokaci, device_info)
                st.success(f"BARKA DA ZUWA {suna}!", icon="✅")
                if shekaru >= 18: st.info(f"AN KARBE KA! KA GIRMA KAKAI AURE ✅")
                else: st.warning(f"BAKA KAI AUREBA. KAJIRA SHEKARA {18 - shekaru} TUKUNNAN ❌")
                if shekaru >= 35: st.error("KAI KA WUCE AURE. KA YI GIRMA SOSAI 😂")
                st.balloons()
            else: st.error("TAF, DA FATAN KA CIKA DUKKAN BAYANAI")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "SHAFIN ADMIN 🔒":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
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
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 SAUKE DATA", df.to_csv(index=False).encode('utf-8'), "masu_aure.csv", "text/csv")
        else: st.info("BABU WANDA YA YI REGISTER TUKUNA")
    elif password: st.error("PASSWORD BA DAIDAI BA NE ❌")
    st.markdown('</div>', unsafe_allow_html=True)
