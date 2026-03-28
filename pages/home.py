import streamlit as st

st.set_page_config(
    page_title="Brain Tumor Detection - Home",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for medical theme
st.markdown("""
<style>
    .main-header {
        color: #0066cc;
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        color: #008080;
        font-size: 1.8em;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .card {
        background-color: #f8f9fa;
        color: #333333;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border-left: 6px solid #0066cc;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .feature-icon {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    .hero-section {
        background: linear-gradient(135deg, #0066cc 0%, #008080 100%);
        color: white;
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
    }
    .stats-card {
        background-color: white;
        color: #333333;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px;
    }
    .btn-primary {
        background-color: #0066cc;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin: 10px;
        transition: background-color 0.3s ease;
    }
    .btn-primary:hover {
        background-color: #004d99;
    }
    .btn-secondary {
        background-color: #008080;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin: 10px;
        transition: background-color 0.3s ease;
    }
    .btn-secondary:hover {
        background-color: #006666;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="main-header">🧠 AI Brain Tumor Detection System</h1>
        <p style="font-size: 1.4em; margin-bottom: 30px;">
        Advanced AI-powered MRI analysis for early tumor detection and accurate classification
        </p>
        <p style="font-size: 1.1em; opacity: 0.9;">
        Revolutionizing medical diagnostics with cutting-edge machine learning technology
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔬 Start Detection", key="detect_btn", use_container_width=True):
            st.switch_page("pages/detection.py")
    with col2:
        if st.button("👤 Patient Login", key="login_btn", use_container_width=True):
            st.switch_page("pages/login.py")
    with col3:
        if st.button("📋 Register", key="register_btn", use_container_width=True):
            st.switch_page("pages/register.py")

    # Features Section
    st.markdown('<h2 class="sub-header" style="text-align: center;">🚀 Our Technology</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="feature-icon">🔬</div>
            <h3>Advanced AI Analysis</h3>
            <p>State-of-the-art deep learning models trained on thousands of MRI scans for accurate tumor detection and classification.</p>
            <ul>
                <li>Glioma Detection</li>
                <li>Meningioma Classification</li>
                <li>Pituitary Tumor Analysis</li>
                <li>No Tumor Verification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="feature-icon">⚡</div>
            <h3>Instant Results</h3>
            <p>Get comprehensive analysis results within seconds. Our optimized algorithms provide fast, reliable diagnostics.</p>
            <ul>
                <li>Real-time Processing</li>
                <li>High Accuracy Scores</li>
                <li>Detailed Confidence Metrics</li>
                <li>Professional Reports</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="feature-icon">🔒</div>
            <h3>Secure & Private</h3>
            <p>Your medical data is protected with enterprise-grade security. HIPAA-compliant platform for healthcare professionals.</p>
            <ul>
                <li>Encrypted Data Storage</li>
                <li>Secure File Upload</li>
                <li>Role-based Access</li>
                <li>Medical Privacy Standards</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Statistics Section
    st.markdown('<h2 class="sub-header" style="text-align: center;">📊 Impact Statistics</h2>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stats-card">
            <h2 style="color: #0066cc; margin: 0;">95%</h2>
            <p style="margin: 5px 0; font-weight: bold;">Accuracy Rate</p>
            <p style="margin: 0; color: #666;">Industry-leading precision</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stats-card">
            <h2 style="color: #008080; margin: 0;">10K+</h2>
            <p style="margin: 5px 0; font-weight: bold;">Scans Analyzed</p>
            <p style="margin: 0; color: #666;">Trusted by professionals</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stats-card">
            <h2 style="color: #28a745; margin: 0;">24/7</h2>
            <p style="margin: 5px 0; font-weight: bold;">Availability</p>
            <p style="margin: 0; color: #666;">Always ready for analysis</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stats-card">
            <h2 style="color: #dc3545; margin: 0;">4</h2>
            <p style="margin: 5px 0; font-weight: bold;">Tumor Types</p>
            <p style="margin: 0; color: #666;">Comprehensive detection</p>
        </div>
        """, unsafe_allow_html=True)

    # How It Works Section
    st.markdown('<h2 class="sub-header" style="text-align: center;">📋 How It Works</h2>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 3em; color: #0066cc;">1️⃣</div>
            <h4>Upload MRI</h4>
            <p>Upload your MRI scan in JPG, PNG, or DICOM format</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 3em; color: #008080;">2️⃣</div>
            <h4>AI Analysis</h4>
            <p>Our AI model analyzes the scan for tumor detection</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 3em; color: #28a745;">3️⃣</div>
            <h4>Get Results</h4>
            <p>Receive detailed analysis with confidence scores</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 3em; color: #dc3545;">4️⃣</div>
            <h4>Consult Doctor</h4>
            <p>Share results with healthcare professionals</p>
        </div>
        """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 40px; border-radius: 15px; text-align: center; margin: 40px 0; color: #333333;">
        <h2 style="color: #0066cc; margin-bottom: 20px;">Ready to Get Started?</h2>
        <p style="font-size: 1.2em; margin-bottom: 30px;">Join thousands of healthcare professionals using our AI-powered diagnostic platform</p>
        <a href="#" class="btn-primary" onclick="document.querySelector('button[key=detect_btn]').click()">Start Detection Now</a>
        <a href="#" class="btn-secondary" onclick="document.querySelector('button[key=register_btn]').click()">Create Account</a>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666; border-top: 1px solid #eee; margin-top: 40px;">
        <p>© 2026 Brain Tumor Detection System | Powered by Advanced AI Technology</p>
        <p>For medical emergencies, please consult qualified healthcare professionals immediately.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()