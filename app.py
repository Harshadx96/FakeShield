import streamlit as st
from datetime import datetime
import requests

# Backend API URLs
LOGIN_URL = "http://192.168.0.227:5000/login"
DETECT_URL = "http://192.168.0.227:5000/detect"

st.set_page_config(page_title="FakeShield", layout="wide")

# Initialize session state for token and errors
if "token" not in st.session_state:
    st.session_state.token = None
if "login_failed" not in st.session_state:
    st.session_state.login_failed = False

# --- Sidebar content shared in login and main pages ---
def render_sidebar():
    with st.sidebar:
        st.markdown("#### 👋 Hello, Digital Guardian!")
        st.markdown("""
Welcome to *FakeShield*, your trusted AI shield to fight deepfakes.

> Guarding truth with the power of AI.
""")
        st.markdown("---")
        st.markdown("### Quick Stats")
        st.metric("Videos Analyzed", "1,205")
        st.metric("Audio Samples Checked", "3,800")
        st.metric("Trusted Clients", "24")
        st.markdown("---")
        st.markdown("#### 💡 Did You Know?")
        st.write("FakeShield continuously learns from viral fakes to protect you better!")
        st.markdown("---")
        st.markdown(f"<span style='color:#ccc;'>{datetime.now():%d-%m-%Y, %H:%M:%S}</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:1.1em;'>☁ 22°C &nbsp;&nbsp; Mostly cloudy</span>", unsafe_allow_html=True)

# --- Right side panel shared in login and main pages ---
def render_right_panel():
    st.markdown(
        """
<div style='background:linear-gradient(120deg,#1f2a3b 80%,#192441 100%); border-radius:18px; padding:1.5em 1em; margin-bottom:18px; color:#d6ebff; box-shadow:0 4px 18px #10172690;'>
<div style="font-size:1.2em; color:#5aeaf7;"><b>🛡 Why Trust FakeShield?</b></div>
<hr style="border-top:1px solid #314459; margin-top:8px; margin-bottom:14px;">
<ul style='padding-left:1.2em; margin-bottom:0;'>
<li>✅ Instantly checks media authenticity</li>
<li>✅ Powerful voice & video analysis</li>
<li>✅ Shareable PDF reports</li>
<li>✅ Private, encrypted and secure</li>
</ul>
</div>
"""
        , unsafe_allow_html=True)

    st.markdown(
        """
<div style='background:linear-gradient(120deg,#262f44 90%,#1a2439 100%); border-radius:18px; padding:1.2em 1em 0.85em 1em; margin-bottom:18px; color:#adefff; box-shadow:0 2px 10px #19244155;'>
<span style="color:#b5fcf7;font-weight:600;">🆕 New:</span>
<hr style="border-top:1px solid #283c53; margin-top:8px; margin-bottom:13px;">
<div><b>Try uploading your first video or audio!</b>
<div style="color:#77b7ff; font-size:0.97em;">Click 'Video Detection' or 'Audio Detection' above to get started.</div></div>
</div>
"""
        , unsafe_allow_html=True)

    st.markdown(
        """
<div style='background:linear-gradient(120deg,#262f44 90%,#1a2439 100%); border-radius:18px; padding:1.1em 1em 0.7em 1em; color:#fff4cd; box-shadow:0 2px 8px #151e2f40;'>
<b>Recent Activity</b>
<hr style="border-top:1px solid #283c53; margin-top:8px; margin-bottom:13px;">
<ul style="padding-left:1.15em; margin-bottom:0;">
<li><span style='color:#abebc6;'>Verified:</span> news_clip_aug25.mp4</li>
<li><span style='color:#f7bdb6;'>Flagged:</span> social_voice_sample.wav</li>
<li><span style='color:#abebc6;'>Verified:</span> webinar_finance.mov</li>
</ul>
</div>
"""
        , unsafe_allow_html=True)

# --- Login Page ---
def render_login_page():
    render_sidebar()

    st.title("🔐 User Login")
    st.markdown("Please sign in to access FakeShield")

    with st.form("login_form"):
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if not username or not password:
            st.warning("Please enter both username and password.")
        else:
            try:
                resp = requests.post(LOGIN_URL, json={"username": username, "password": password})
                if resp.status_code == 200 and "access_token" in resp.json():
                    st.session_state.token = resp.json()["access_token"]
                    st.session_state.login_failed = False
                    st.experimental_rerun()
                else:
                    st.session_state.login_failed = True
            except Exception as e:
                st.error(f"Login request failed: {e}")

    if st.session_state.get("login_failed", False):
        st.error("Login failed. Please check your credentials.")

    render_right_panel()

# --- Main App Page ---
def render_main_app():
    render_sidebar()

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h1 style='margin-bottom:4px;'>FakeShield</h1>", unsafe_allow_html=True)
        st.markdown("<div style='color:#b8cbe7;'>Deepfake Video & Voice Synthesis Detection</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align:right; color:#6debf7;'>📅 {datetime.now():%Y-%m-%d} &nbsp; 🕒 {datetime.now():%H:%M:%S}</div>", unsafe_allow_html=True)

    st.write("")

    main_col, right_col = st.columns([2.1, 1])

    with main_col:
        tabs = st.tabs(["About", "Video Detection", "Audio Detection"])

        with tabs[0]:
            st.subheader("About FakeShield")
            st.markdown(
"""
Detect the Future. Protect the Truth.

FakeShield is not just a deepfake detector—it’s your digital truth defender.

*Innovation Highlights*

- 🟣 Advanced multimodal AI that sees and hears through deception
- ⚡ Lightning-fast forensic analysis for video and audio fakes
- 🗂 Intuitive result cards and downloadable reports for sharing

*Who needs FakeShield?*

- Media & journalism teams verifying viral videos
- Legal, compliance, and security pros seeking evidence
- Content creators and digital citizens staying ahead
"""
            )

        with tabs[1]:
            st.subheader("Video Detection")
            uploaded_vid = st.file_uploader("Upload a video file (mp4, avi, mov)", type=["mp4", "avi", "mov"], key="video_upload")
            if uploaded_vid:
                st.video(uploaded_vid)
                st.info("✔ Video uploaded! Sending to backend for analysis...")

                files = {"file": (uploaded_vid.name, uploaded_vid, uploaded_vid.type)}
                headers = {"Authorization": f"Bearer {st.session_state.token}"}
                try:
                    response = requests.post(DETECT_URL, files=files, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        st.success("Detection Result:")
                        st.json(result)
                    else:
                        st.error("Detection failed.")
                        st.text(response.text)
                except Exception as e:
                    st.error(f"Backend request error: {e}")

            st.markdown("<div style='color:#87deff;'>Detect manipulated visuals, realistic fakes, and ensure source credibility for any video clip.</div>", unsafe_allow_html=True)

        with tabs[2]:
            st.subheader("Audio Detection")
            uploaded_audio = st.file_uploader("Upload an audio file (wav, mp3, m4a)", type=["wav", "mp3", "m4a"], key="audio_upload")
            if uploaded_audio:
                st.audio(uploaded_audio)
                st.info("✔ Audio uploaded! Sending to backend for analysis...")

                files = {"file": (uploaded_audio.name, uploaded_audio, uploaded_audio.type)}
                headers = {"Authorization": f"Bearer {st.session_state.token}"}
                try:
                    response = requests.post(DETECT_URL, files=files, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        st.success("Detection Result:")
                        st.json(result)
                    else:
                        st.error("Detection failed.")
                        st.text(response.text)
                except Exception as e:
                    st.error(f"Backend request error: {e}")

            st.markdown("<div style='color:#fcc47a;'>Spot synthesized voices, altered statements, and identity theft risks in any recording.</div>", unsafe_allow_html=True)

    with right_col:
        render_right_panel()

# --- Footer ---
st.markdown(
    """
<div style='margin-top:48px; text-align:right; color:#6c8db3; font-size:0.87em;'>
FakeShield © 2025 &nbsp; | &nbsp; Demo at <b>KuruKshetra-25( HackFest )</b>
</div>
""",
    unsafe_allow_html=True,
)

# --- Main logic ---
if st.session_state.token is None:
    render_login_page()
else:
    render_main_app()
