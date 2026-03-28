import streamlit as st
import time

st.set_page_config(
    page_title="Brain Tumor Detection - Register",
    page_icon="📋",
    layout="centered"
)

# Custom CSS for register page
st.markdown("""
<style>
    .register-container {
        max-width: 500px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f8f9fa;
        color: #333333;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .register-header {
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
    .form-row {
        display: flex;
        gap: 15px;
    }
    .form-row .form-group {
        flex: 1;
    }
    .btn-register {
        width: 100%;
        padding: 12px;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        margin: 10px 0;
        transition: background-color 0.3s ease;
    }
    .btn-register:hover {
        background-color: #218838;
    }
    .terms-checkbox {
        display: flex;
        align-items: center;
        margin: 15px 0;
    }
    .terms-checkbox input {
        margin-right: 10px;
    }
    .terms-link {
        color: #0066cc;
        text-decoration: none;
    }
    .terms-link:hover {
        text-decoration: underline;
    }
    .login-link {
        text-align: center;
        margin-top: 20px;
    }
    .login-link a {
        color: #0066cc;
        text-decoration: none;
        font-weight: bold;
    }
    .login-link a:hover {
        text-decoration: underline;
    }
    .password-strength {
        margin-top: 5px;
        font-size: 0.9em;
    }
    .strength-weak {
        color: #dc3545;
    }
    .strength-medium {
        color: #ffc107;
    }
    .strength-strong {
        color: #28a745;
    }
</style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    """Check password strength"""
    if len(password) < 6:
        return "weak", "Password too short (minimum 6 characters)"
    elif len(password) < 8:
        return "medium", "Medium strength - consider adding numbers/symbols"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "strong", "Strong password"
    else:
        return "medium", "Add numbers for better security"

def main():
    st.markdown('<h1 class="register-header">📋 Patient Registration</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="register-container">
        <p style="text-align: center; color: #666; margin-bottom: 30px;">
        Create your account to access personalized brain tumor detection services
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Registration Form
    with st.form("register_form"):
        st.markdown("### Personal Information")

        # Name fields
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name", placeholder="Enter your first name")
        with col2:
            last_name = st.text_input("Last Name", placeholder="Enter your last name")

        # Contact information
        email = st.text_input("Email Address", placeholder="your.email@example.com")
        phone = st.text_input("Phone Number (Optional)", placeholder="+1 (555) 123-4567")

        st.markdown("### Account Security")
        password = st.text_input("Password", type="password", placeholder="Create a strong password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")

        # Password strength indicator
        if password:
            strength, message = check_password_strength(password)
            st.markdown(f"""
            <div class="password-strength strength-{strength}">
                Password Strength: {message}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Medical Information")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, value=25)
        with col2:
            gender = st.selectbox("Gender", ["Select Gender", "Male", "Female", "Other", "Prefer not to say"])

        # Medical conditions (optional)
        medical_conditions = st.text_area(
            "Medical Conditions (Optional)",
            placeholder="List any relevant medical conditions or allergies...",
            height=80
        )

        # Terms and conditions
        agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
        agree_medical = st.checkbox("I understand this is for diagnostic assistance only")

        submitted = st.form_submit_button("Create Account", use_container_width=True)

        if submitted:
            # Validation
            errors = []

            if not first_name or not last_name:
                errors.append("Please enter your full name")
            if not email:
                errors.append("Please enter your email address")
            if not password:
                errors.append("Please enter a password")
            if password != confirm_password:
                errors.append("Passwords do not match")
            if gender == "Select Gender":
                errors.append("Please select your gender")
            if not agree_terms:
                errors.append("Please agree to the Terms of Service")
            if not agree_medical:
                errors.append("Please confirm understanding of medical disclaimer")

            # Email validation
            if email and "@" not in email:
                errors.append("Please enter a valid email address")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Mock registration success
                with st.spinner("Creating your account..."):
                    time.sleep(2)

                st.success("🎉 Account created successfully!")

                # Set session state
                st.session_state.user_data = {
                    'name': f"{first_name} {last_name}",
                    'email': email,
                    'phone': phone,
                    'age': age,
                    'gender': gender,
                    'medical_conditions': medical_conditions
                }
                st.session_state.logged_in = True
                st.session_state.user_role = 'patient'
                st.session_state.scan_history = []

                st.markdown("""
                <div style="background-color: #d4edda; border: 1px solid #c3e6cb; border-radius: 5px; padding: 15px; margin: 20px 0; color: #333333;">
                    <strong>✅ Registration Complete!</strong><br>
                    Welcome to Brain Tumor Detection System. You can now upload MRI scans and access your medical history.
                </div>
                """, unsafe_allow_html=True)

                # Redirect after short delay
                time.sleep(2)
                st.switch_page("pages/dashboard.py")

    # Additional Links
    st.markdown("""
    <div class="login-link">
        Already have an account? <a href="#" onclick="document.querySelector('button[key=login_redirect]').click()">Login here</a>
    </div>
    """, unsafe_allow_html=True)

    # Terms and Privacy Links
    st.markdown("""
    <div style="text-align: center; margin: 20px 0; font-size: 0.9em; color: #666;">
        By registering, you agree to our <a href="#" style="color: #0066cc;">Terms of Service</a> and <a href="#" style="color: #0066cc;">Privacy Policy</a>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Home", key="home_redirect", use_container_width=True):
            st.switch_page("pages/home.py")
    with col2:
        if st.button("👤 Login", key="login_redirect", use_container_width=True):
            st.switch_page("pages/login.py")
    with col3:
        if st.button("🔬 Quick Analysis", use_container_width=True):
            st.switch_page("pages/detection.py")

if __name__ == "__main__":
    main()