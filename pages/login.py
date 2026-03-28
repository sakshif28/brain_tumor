import streamlit as st
import time

st.set_page_config(
    page_title="Brain Tumor Detection - Login",
    page_icon="👤",
    layout="centered"
)

# Custom CSS for login page
st.markdown("""
<style>
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f8f9fa;
        color: #333333;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .login-header {
        color: #0066cc;
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .form-group {
        margin-bottom: 20px;
    }
    .form-label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
        color: #333;
    }
    .form-input {
        width: 100%;
        padding: 12px;
        border: 2px solid #ddd;
        border-radius: 8px;
        font-size: 1em;
        transition: border-color 0.3s ease;
    }
    .form-input:focus {
        outline: none;
        border-color: #0066cc;
        box-shadow: 0 0 5px rgba(0, 108, 204, 0.3);
    }
    .btn-login {
        width: 100%;
        padding: 12px;
        background-color: #0066cc;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        margin: 10px 0;
        transition: background-color 0.3s ease;
    }
    .btn-login:hover {
        background-color: #004d99;
    }
    .btn-secondary {
        width: 100%;
        padding: 12px;
        background-color: #008080;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        margin: 10px 0;
        transition: background-color 0.3s ease;
    }
    .btn-secondary:hover {
        background-color: #006666;
    }
    .divider {
        text-align: center;
        margin: 20px 0;
        position: relative;
    }
    .divider::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 0;
        right: 0;
        height: 1px;
        background-color: #ddd;
    }
    .divider span {
        background-color: #f8f9fa;
        padding: 0 10px;
        color: #666;
    }
    .role-selector {
        display: flex;
        margin-bottom: 20px;
        background-color: white;
        border-radius: 8px;
        overflow: hidden;
        border: 2px solid #ddd;
    }
    .role-option {
        flex: 1;
        padding: 12px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        background-color: white;
    }
    .role-option.active {
        background-color: #0066cc;
        color: white;
    }
    .role-option:hover:not(.active) {
        background-color: #f0f8ff;
    }
    .forgot-password {
        text-align: center;
        margin-top: 15px;
    }
    .forgot-password a {
        color: #0066cc;
        text-decoration: none;
    }
    .forgot-password a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="login-header">👤 Login to Brain Tumor Detection</h1>', unsafe_allow_html=True)

    # Initialize session state
    if 'login_role' not in st.session_state:
        st.session_state.login_role = 'patient'

    st.markdown("""
    <div class="login-container">
        <div class="role-selector">
            <button class="role-option {}" onclick="document.getElementById('patient_role').click()">👤 Patient</button>
            <button class="role-option {}" onclick="document.getElementById('admin_role').click()">👨‍⚕️ Admin</button>
        </div>
    """.format(
        'active' if st.session_state.login_role == 'patient' else '',
        'active' if st.session_state.login_role == 'admin' else ''
    ), unsafe_allow_html=True)

    # Hidden buttons for role selection
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Patient", key="patient_role", help="Login as a patient"):
            st.session_state.login_role = 'patient'
            st.rerun()
    with col2:
        if st.button("Admin", key="admin_role", help="Login as an administrator"):
            st.session_state.login_role = 'admin'
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Login Form
    with st.form("login_form"):
        st.markdown("### {} Login".format("Patient" if st.session_state.login_role == 'patient' else "Administrator"))

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address",
            help="Use any email format for demo purposes"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            help="Use any password for demo purposes"
        )

        # Additional fields for admin
        if st.session_state.login_role == 'admin':
            st.markdown("""
            <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; padding: 10px; margin: 10px 0; color: #333333;">
                <strong>⚠️ Restricted Access:</strong> This section is for authorized medical personnel only.
            </div>
            """, unsafe_allow_html=True)

        submitted = st.form_submit_button("Login", use_container_width=True)

        if submitted:
            if email and password:
                # Mock authentication - accept any email/password
                st.success("Login successful! Redirecting...")

                # Set session state
                st.session_state.logged_in = True
                st.session_state.user_role = st.session_state.login_role
                st.session_state.user_email = email

                # Mock user data
                if st.session_state.login_role == 'patient':
                    st.session_state.user_data = {
                        'name': 'Demo Patient',
                        'email': email,
                        'age': 35,
                        'gender': 'Not specified'
                    }
                    st.session_state.scan_history = []
                else:
                    st.session_state.admin_data = {
                        'patients': [],
                        'scans': []
                    }

                # Redirect after short delay
                time.sleep(1)

                if st.session_state.login_role == 'patient':
                    st.switch_page("pages/dashboard.py")
                else:
                    st.switch_page("pages/admin_dashboard.py")

            else:
                st.error("Please enter both email and password")

    # Additional Options
    st.markdown("""
    <div class="divider">
        <span>or</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Create Account", use_container_width=True):
            st.switch_page("pages/register.py")

    with col2:
        if st.button("🔬 Quick Analysis", use_container_width=True):
            st.switch_page("pages/detection.py")

    # Forgot Password
    st.markdown("""
    <div class="forgot-password">
        <a href="#">Forgot your password?</a>
    </div>
    """, unsafe_allow_html=True)

    # Demo Credentials
    with st.expander("🔑 Demo Credentials"):
        st.markdown("""
        **For Testing Purposes:**

        **Patient Login:**
        - Email: patient@demo.com
        - Password: demo123

        **Admin Login:**
        - Email: admin@demo.com
        - Password: admin123

        *Note: Any email/password combination will work for demo purposes.*
        """)

    # Navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.switch_page("pages/home.py")
    with col2:
        if st.button("ℹ️ About", use_container_width=True):
            st.switch_page("pages/about.py")

if __name__ == "__main__":
    main()