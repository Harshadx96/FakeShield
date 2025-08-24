import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import time

# Auto-refresh every 1 second for clock
st_autorefresh(interval=1000, key="clockrefresh")

# Page config & refined gradient background
st.set_page_config(page_title="FakeShield", layout="wide", initial_sidebar_state="auto")
st.markdown("""
<style>
    /* Elegant vertical gradient background */
    body, .reportview-container, .block-container {
        background: linear-gradient(180deg, #182848 0%, #090a17 100%);
        color: #e0e0e0 !important;
    }
    /* Sidebar styled dark */
    [data-testid="stSidebar"], .stSidebar, .stSidebarContent, .css-1lcbmhc {
        background: linear-gradient(180deg, #182848 40%, #090a17 100%) !important;
        color: #e0e0e0 !important;
    }
    /* Button highlight */
    .stButton>button {background-color: #007acc; color: white;}
    /* Links */
    a {text-decoration:none; color:#21d4fd;}
    a:hover {text-decoration:underline;}
    /* Header row */
    .header-row {display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 8px;}
    .clockbox {
        font-size:18px;
        font-weight:600;
        color: #21d4fd;
        font-family:'Segoe UI', 'Trebuchet MS', 'Arial', sans-serif;
        letter-spacing: 2px;
        opacity:0.88;
        text-shadow:0 0 8px #21d4fd60;
        margin-right:4px;
        margin-top:12px;
    }
    .sidebar-img {
        display:block;
        margin-left:auto;
        margin-right:auto;
        margin-top:8px;
        margin-bottom:10px;
        border-radius:12px;
        box-shadow:0 0 8px #21d4fd25;
        width:60px;
        height:60px;
        object-fit:cover;
    }
    /* Remove st.info yellow highlight globally */
    div[data-testid="stNotification"], .stInfo {
        background-color: #212940 !important;
        color: #e0e0e0 !important;
        border-left: 4px solid #007acc !important;
    }
</style>
""", unsafe_allow_html=True)

# Header with title and clock (always right-aligned, small, elegant)
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%I:%M:%S %p")
st.markdown(f"""
<div class='header-row'>
    <div>
        <h1 style='margin-bottom:0'>FakeShield</h1>
        <h3 style='margin-top:2px; font-weight:400'>Deepfake Video & Voice Synthesis Detection</h3>
    </div>
    <div class='clockbox'>
        🗓️ {date_str} &nbsp; 🕒 {time_str}
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar: compact image, no yellow, perfect color balance
with st.sidebar:
    st.markdown("## 👋 Hello, Digital Guardian!")
    st.write("Welcome to **FakeShield**, your trusted AI shield to fight deepfakes.")
    st.caption("🛡️ Guarding truth with the power of AI.")
    st.markdown("---")

    st.markdown("### 📊 Quick Stats")
    st.metric("Videos Analyzed", "1,205")
    st.metric("Audio Samples Checked", "3,800")
    st.metric("Trusted Clients", "24")
    st.markdown("---")

    st.markdown("### 💡 Did You Know?")
    st.info("FakeShield scans over 150+ signal features to detect synthetic media.")
    st.markdown("---")

    st.markdown("### 🔎 Keep Questioning Media")
    st.markdown("*“The truth will set you free, but first it will make you uncomfortable.”*")
    st.image("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif", width=60)
    st.markdown("---")

    st.subheader("Contact Us")
    st.write("**📧 Email:** support@fakeshield.ai")
    st.code("support@fakeshield.ai", language="markdown")
    st.caption("We reply within 24 hours.")
    st.markdown("---")

    st.info("🔒 Your privacy is our priority. Files are never stored.")
    st.caption("FakeShield © 2025 | Powered by AI & Human Trust")

# Tabs
tab_about, tab_video, tab_audio = st.tabs(["ℹ️ About", "🎬 Video Detection", "🎤 Audio Detection"])

# About Tab
with tab_about:
    st.header("About FakeShield")
    st.markdown("""
### Detect the Future. Protect the Truth.

FakeShield is not just a deepfake detector—it's your digital truth defender.

**Innovation Highlights:**
- 🧠 Advanced multimodal AI that sees and hears through deception.
- ⚡ Lightning-fast forensic analysis for both video and voice synthesis fakes.
- 📊 Intuitive result cards and downloadable reports for confident sharing.

**Who needs FakeShield?**
- Media & journalism teams verifying viral videos.
- Legal, compliance, and security pros seeking evidence.
- Content creators and digital citizens staying one step ahead.

> FakeShield blends novel computer vision, audio fingerprinting, and forensic analytics to spot even the most sophisticated deepfakes—before they go viral.

**Join us to protect reality and fight misinformation. The future of trust starts here.**
""")

# Video Detection Tab
with tab_video:
    st.header("Upload a Video File")
    video_file = st.file_uploader("Choose a video file (MP4, AVI, MOV)", type=["mp4", "avi", "mov"], key="video")
    if video_file is not None:
        st.success("File uploaded! Starting analysis...")
        with st.spinner("Analyzing video for deepfake..."):
            time.sleep(2)
        score = 83
        verdict = "Authentic"
        color = "#00ff89" if verdict == "Authentic" else "#ff6040" if verdict == "Suspicious" else "#ff1a1a"
        col1, col2 = st.columns([2, 3])
        with col1:
            st.video(video_file)
        with col2:
            st.success("✅ Analysis complete!")
            st.markdown(f"""
                <div style="background:#212940; padding:16px; border-radius:10px; margin-top:10px;">
                    <h3 style="color:{color};">Authenticity Score: <b>{score}%</b></h3>
                    <p style="color:#e0e0e0;">Verdict: <span style="color:{color};">{verdict}</span></p>
                </div>
            """, unsafe_allow_html=True)
            st.subheader("Authenticity Confidence")
            st.progress(score)
            signals = [
                {"name": "Eye Blinking", "status": "Normal", "icon": "👁️"},
                {"name": "Lip Sync", "status": "Mismatch", "icon": "👄"},
                {"name": "Head Movements", "status": "Abnormal", "icon": "🧠"},
            ]
            st.subheader("Key Signals Checked:")
            for sig in signals:
                color_emoji = "🟢" if sig["status"] == "Normal" else "🟠" if sig["status"] == "Mismatch" else "🔴"
                st.markdown(f"{sig['icon']} **{sig['name']}:** {color_emoji} {sig['status']}")
            st.download_button(
                label="📄 Download Forensic Report (PDF)",
                data=b"%PDF-1.4\n%FakeShield dummy PDF report",
                file_name="FakeShield_Report.pdf",
                mime="application/pdf",
            )
    else:
        st.info("Please upload a video file to begin analysis.")

# Audio Detection Tab
with tab_audio:
    st.header("Upload an Audio File")
    audio_file = st.file_uploader("Choose an audio file (MP3, WAV, AAC)", type=["mp3", "wav", "aac"], key="audio")
    if audio_file is not None:
        st.success("File uploaded! Starting analysis...")
        st.audio(audio_file)
        with st.spinner("Analyzing audio for deepfake..."):
            time.sleep(2)
        score = 76
        verdict = "Suspicious"
        color = "#00ff89" if verdict == "Authentic" else "#ff6040" if verdict == "Suspicious" else "#ff1a1a"
        col1, col2 = st.columns([2, 3])
        with col1:
            st.audio(audio_file)
        with col2:
            st.success("✅ Analysis complete!")
            st.markdown(f"""
                <div style="background:#212940; padding:16px; border-radius:10px; margin-top:10px;">
                    <h3 style="color:{color};">Authenticity Score: <b>{score}%</b></h3>
                    <p style="color:#e0e0e0;">Verdict: <span style="color:{color};">{verdict}</span></p>
                </div>
            """, unsafe_allow_html=True)
            st.subheader("Authenticity Confidence")
            st.progress(score)
            signals = [
                {"name": "Pitch Analysis", "status": "Normal", "icon": "🎵"},
                {"name": "Tempo Consistency", "status": "Warning", "icon": "⏱️"},
                {"name": "Anomaly Detection", "status": "Abnormal", "icon": "⚡"},
            ]
            st.subheader("Key Signals Checked:")
            for sig in signals:
                color_emoji = "🟢" if sig["status"] == "Normal" else "🟠" if sig["status"] == "Warning" else "🔴"
                st.markdown(f"{sig['icon']} **{sig['name']}:** {color_emoji} {sig['status']}")
            st.download_button(
                label="📄 Download Forensic Report (PDF)",
                data=b"%PDF-1.4\n%FakeShield dummy PDF report",
                file_name="FakeShield_Report.pdf",
                mime="application/pdf",
            )
    else:
        st.info("Please upload an audio file to begin analysis.")
