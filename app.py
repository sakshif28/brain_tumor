import streamlit as st

# Set page config
st.set_page_config(
    page_title="Brain Tumor Detection System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'scan_history' not in st.session_state:
    st.session_state.scan_history = []
if 'admin_data' not in st.session_state:
    st.session_state.admin_data = {
        'patients': [],
        'scans': []
    }

# Navigation
pages = [
    st.Page("pages/home.py", title="Home", icon="🏠"),
    st.Page("pages/detection.py", title="Detection", icon="🔬"),
    st.Page("pages/about.py", title="About", icon="ℹ️"),
    st.Page("pages/login.py", title="Login", icon="👤"),
    st.Page("pages/register.py", title="Register", icon="📋"),
]

# Add authenticated pages based on user role
if st.session_state.logged_in:
    if st.session_state.user_role == 'patient':
        pages.append(st.Page("pages/dashboard.py", title="My Dashboard", icon="📊"))
    elif st.session_state.user_role == 'admin':
        pages.append(st.Page("pages/admin_dashboard.py", title="Admin Panel", icon="👨‍⚕️"))

pg = st.navigation(pages)
pg.run()