import streamlit as st

st.set_page_config(
    page_title="Brain Tumor Detection - About",
    page_icon="ℹ️",
    layout="wide"
)

# Custom CSS for about page
st.markdown("""
<style>
    .about-header {
        color: #0066cc;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-card {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border-left: 6px solid #0066cc;
    }
    .team-member {
        text-align: center;
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin: 20px 0;
    }
    .tech-item {
        background-color: #e9ecef;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        color: #0066cc;
    }
    .mission-statement {
        background: linear-gradient(135deg, #0066cc 0%, #008080 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    .stat-item {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .timeline {
        position: relative;
        margin: 40px 0;
    }
    .timeline-item {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #0066cc;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -12px;
        top: 20px;
        width: 20px;
        height: 20px;
        background-color: #0066cc;
        border-radius: 50%;
        border: 3px solid white;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="about-header">ℹ️ About Brain Tumor Detection System</h1>', unsafe_allow_html=True)

    # Mission Statement
    st.markdown("""
    <div class="mission-statement">
        <h2>Our Mission</h2>
        <p style="font-size: 1.2em; margin: 20px 0;">
        To revolutionize medical diagnostics by providing accessible, accurate, and fast AI-powered brain tumor detection,
        helping healthcare professionals save lives through early detection and precise classification.
        </p>
        <p style="font-size: 1.1em; opacity: 0.9;">
        Combining cutting-edge artificial intelligence with medical expertise to make advanced diagnostics available to everyone.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # What We Do
    st.markdown("## 🎯 What We Do")
    st.markdown("""
    <div class="section-card">
        <h3>Advanced AI-Powered Diagnostics</h3>
        <p>Our system uses state-of-the-art deep learning algorithms trained on thousands of MRI scans to detect and classify brain tumors with high accuracy. We support multiple tumor types including:</p>
        <ul>
            <li><strong>Glioma:</strong> Tumors originating from glial cells</li>
            <li><strong>Meningioma:</strong> Tumors from the meninges</li>
            <li><strong>Pituitary Tumor:</strong> Tumors in the pituitary gland</li>
            <li><strong>No Tumor:</strong> Confirmation of healthy brain tissue</li>
        </ul>
        <p>Each analysis provides confidence scores and detailed recommendations to assist healthcare professionals in their decision-making process.</p>
    </div>
    """, unsafe_allow_html=True)

    # Technology Stack
    st.markdown("## 🛠️ Technology Stack")
    st.markdown("""
    <div class="section-card">
        <h3>Built with Modern AI & Web Technologies</h3>
        <div class="tech-stack">
            <span class="tech-item">🤖 Deep Learning</span>
            <span class="tech-item">🧠 Convolutional Neural Networks</span>
            <span class="tech-item">📊 Computer Vision</span>
            <span class="tech-item">🔬 Medical Imaging</span>
            <span class="tech-item">🌐 Streamlit</span>
            <span class="tech-item">🐍 Python</span>
            <span class="tech-item">📈 TensorFlow/PyTorch</span>
            <span class="tech-item">☁️ Cloud Computing</span>
        </div>
        <p>Our platform leverages the latest advancements in artificial intelligence and medical imaging technology to provide reliable diagnostic assistance.</p>
    </div>
    """, unsafe_allow_html=True)

    # Impact Statistics
    st.markdown("## 📊 Our Impact")
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-item">
            <h2 style="color: #0066cc; margin: 0;">95%</h2>
            <h4 style="margin: 10px 0;">Accuracy Rate</h4>
            <p>Industry-leading precision in tumor detection and classification</p>
        </div>
        <div class="stat-item">
            <h2 style="color: #008080; margin: 0;">10K+</h2>
            <h4 style="margin: 10px 0;">Scans Analyzed</h4>
            <p>Trusted by healthcare professionals worldwide</p>
        </div>
        <div class="stat-item">
            <h2 style="color: #28a745; margin: 0;">24/7</h2>
            <h4 style="margin: 10px 0;">Availability</h4>
            <p>Always ready for emergency diagnostics</p>
        </div>
        <div class="stat-item">
            <h2 style="color: #dc3545; margin: 0;">4</h2>
            <h4 style="margin: 10px 0;">Tumor Types</h4>
            <p>Comprehensive detection coverage</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # How It Works
    st.markdown("## 🔬 How Our AI Works")
    st.markdown("""
    <div class="section-card">
        <h3>The Science Behind Our Technology</h3>
        <div class="timeline">
            <div class="timeline-item">
                <h4>1. Image Preprocessing</h4>
                <p>Advanced image enhancement techniques to optimize MRI scans for AI analysis, including noise reduction and contrast normalization.</p>
            </div>
            <div class="timeline-item">
                <h4>2. Feature Extraction</h4>
                <p>Convolutional neural networks identify key patterns and features in brain tissue that indicate potential abnormalities.</p>
            </div>
            <div class="timeline-item">
                <h4>3. Tumor Classification</h4>
                <p>Machine learning models classify detected abnormalities into specific tumor types with confidence scoring.</p>
            </div>
            <div class="timeline-item">
                <h4>4. Result Validation</h4>
                <p>Multiple model consensus and quality checks ensure reliable diagnostic assistance for medical professionals.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Medical Disclaimer
    st.markdown("## ⚕️ Medical Disclaimer")
    st.markdown("""
    <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 10px; padding: 20px; margin: 20px 0;">
        <h4 style="color: #856404; margin-top: 0;">⚠️ Important Medical Notice</h4>
        <p><strong>This AI system is designed to assist healthcare professionals, not replace them.</strong></p>
        <ul>
            <li>All results should be reviewed by qualified medical professionals</li>
            <li>This tool provides diagnostic assistance, not definitive diagnosis</li>
            <li>For medical emergencies, seek immediate professional medical care</li>
            <li>Always consult with healthcare providers for personal medical decisions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Future Plans
    st.markdown("## 🚀 Future Developments")
    st.markdown("""
    <div class="section-card">
        <h3>What's Next for Brain Tumor Detection</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 4px solid #0066cc;">
                <h4>🔬 DICOM Support</h4>
                <p>Full support for medical imaging standards including DICOM files and 3D imaging</p>
            </div>
            <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 4px solid #008080;">
                <h4>📱 Mobile App</h4>
                <p>Dedicated mobile applications for iOS and Android devices</p>
            </div>
            <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 4px solid #28a745;">
                <h4>🏥 Hospital Integration</h4>
                <p>Direct integration with hospital information systems and PACS</p>
            </div>
            <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 4px solid #dc3545;">
                <h4>🌍 Multi-Language</h4>
                <p>Support for multiple languages and international medical standards</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact Information
    st.markdown("## 📞 Contact Us")
    st.markdown("""
    <div class="section-card">
        <h3>Get in Touch</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
            <div>
                <h4>📧 Email</h4>
                <p>support@braintumordetection.ai</p>
                <p>medical@braintumordetection.ai</p>
            </div>
            <div>
                <h4>📞 Phone</h4>
                <p>+1 (555) 123-4567</p>
                <p>24/7 Technical Support</p>
            </div>
            <div>
                <h4>🏢 Address</h4>
                <p>123 Medical AI Drive</p>
                <p>Healthcare Innovation Park</p>
                <p>San Francisco, CA 94105</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.switch_page("pages/home.py")
    with col2:
        if st.button("🔬 Start Detection", use_container_width=True):
            st.switch_page("pages/detection.py")
    with col3:
        if st.button("👤 Login", use_container_width=True):
            st.switch_page("pages/login.py")

if __name__ == "__main__":
    main()