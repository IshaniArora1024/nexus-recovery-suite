import streamlit as st
import pandas as pd
import urllib.parse
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# --- 1. SECURE CONFIGURATION ---
# Load local .env file for development; on Cloud, it uses Secrets
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Safety Check: Stop app if Key is missing
if not GEMINI_KEY:
    st.error("⚠️ Security Alert: API Key not detected. Please add GEMINI_API_KEY to your Secrets/Environment Variables.")
    st.stop()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Nexus Global | Intelligence", layout="wide", page_icon="🛡️")

# --- 3. ENTERPRISE OBSIDIAN DESIGN SYSTEM ---
st.markdown("""
<style>
/* Remove default Streamlit gray panels */
[data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] { display: none; }

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 0rem !important;
    max-width: 95% !important;
}

.stApp { background-color: #050505; color: #FFFFFF; font-family: 'Inter', sans-serif; }

.nexus-branding {
    font-weight: 900; font-size: 3.5rem; color: #39ace7;
    text-shadow: 0 0 20px rgba(57, 172, 231, 0.6);
    letter-spacing: -2px; margin-bottom: 0px;
}

div[data-testid="stMetric"] {
    background: #0D0D0D; border: 1px solid #1F1F1F;
    padding: 20px; border-radius: 12px; text-align: center;
}
div[data-testid="stMetricLabel"] { color: #888888 !important; font-size: 0.9rem !important; font-weight: 600 !important; }
div[data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 2.2rem !important; font-weight: 800 !important; }

.header-box {
    background-color: #1A1A1A; border: 1px solid #2A2A2A;
    padding: 12px 25px; border-radius: 10px 10px 0 0; margin-bottom: 0px;
}

div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="stDataFrame"]),
div[data-testid="stVerticalBlock"] > div:has(> div.stSelectbox),
div[data-testid="stVerticalBlock"] > div:has(> textarea),
div[data-testid="stVerticalBlock"] > div:has(> button) {
    background: #0A0A0A; border: 1px solid #1A1A1A;
    border-radius: 0 0 16px 16px; padding: 35px; margin-top: 0px;
}

div.stButton > button {
    background-color: #FFFFFF; color: #000000; border-radius: 6px;
    font-weight: 800; height: 3.5rem; width: 100%;
    text-transform: uppercase; letter-spacing: 1px; border: none;
}
div.stButton > button:hover { background-color: #39ace7; color: white; box-shadow: 0 0 15px rgba(57, 172, 231, 0.5); }

.stDataFrame { border: 1px solid #1A1A1A !important; border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# --- 4. AI SETUP ---
client = genai.Client(api_key=GEMINI_KEY, http_options=types.HttpOptions(api_version="v1"))

def generate_recovery_outreach(name, review):
    prompt = f"Senior VIP Relations Lead at Nexus Global. Write 3-sentence apology to {name} for: {review}. Offer 20% discount RESET20."
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text

# --- 5. UI LAYOUT ---
st.markdown('<h1 class="nexus-branding">🛡️ NEXUS GLOBAL</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#555555; font-weight:600; margin-top:-10px; letter-spacing:2px;">SENTIMENT INTELLIGENCE COMMAND</p>', unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
k1.metric("RESPONSE RATE", "99.4%", "OPTIMAL")
k2.metric("SENTIMENT INDEX", "0.24", "STABLE")
k3.metric("CRITICAL CASES", "4", "ACTION REQ")
k4.metric("AI PRECISION", "98.7%", "ELITE")

st.write("---")
df = pd.read_csv("reviews.csv")

col_left, col_right = st.columns([1.5, 1], gap="large")

with col_left:
    st.markdown('<div class="header-box"><h4 style="margin:0;">📂 CLIENT INTELLIGENCE FEED</h4></div>', unsafe_allow_html=True)
    st.dataframe(df.style.set_properties(**{"background-color": "#050505", "color": "#FFFFFF", "border-color": "#1A1A1A"}), use_container_width=True, height=820)

with col_right:
    st.markdown('<div class="header-box"><h4 style="margin:0;">⚡ ACTION CENTER</h4></div>', unsafe_allow_html=True)
    target = st.selectbox("IDENTIFY CLIENT", df["Customer_Name"])
    cust = df[df["Customer_Name"] == target].iloc[0]
    
    priority_level = "Critical" if cust["Past_Purchases"] > 15 else "High"
    st.markdown(f"**Priority: {priority_level} · {cust['Customer_Tier']} Customer**")

    st.markdown(f"""<div style="background:#111111; padding:20px; border-radius:10px; border-left:5px solid #39ace7; margin-bottom:25px;">
        <p style="color:#666666; font-size:0.8rem; font-weight:700; text-transform:uppercase;">Customer Review</p>
        <p style="font-size:1.1rem; color:#FFFFFF; margin-top:5px; line-height:1.5;"><i>"{cust['Review_Text']}"</i></p>
    </div>""", unsafe_allow_html=True)

    if st.button("EXECUTE AI DRAFT"):
        st.session_state.nexus_final_msg = generate_recovery_outreach(target, cust["Review_Text"])

    if "nexus_final_msg" in st.session_state:
        msg = st.text_area("OUTREACH PACKAGE", value=st.session_state.nexus_final_msg, height=280)
        mailto = f"mailto:{cust.get('Email', 'client@nexus.com')}?subject=Formal Resolution&body={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{mailto}" target="_blank" style="text-decoration:none;"><div style="background:#39ace7; color:white; text-align:center; padding:18px; border-radius:8px; font-weight:800; margin-top:20px; box-shadow:0 4px 20px rgba(57,172,231,0.4);">✉️ DISPATCH VIA ENTERPRISE MAIL</div></a>', unsafe_allow_html=True)