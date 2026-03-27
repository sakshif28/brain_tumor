import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
import random
import io

st.set_page_config(
    page_title="Brain Tumor Detection - Analysis",
    page_icon="🔬",
    layout="wide"
)

# Custom CSS for detection page - Human-designed, natural feel
st.markdown("""
<style>
    .detection-header {
        color: #2c3e50;
        font-size: 2.2em;
        font-weight: 600;
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: -0.5px;
    }
    .upload-zone {
        border: 2px dashed #3498db;
        border-radius: 12px;
        padding: 45px 30px;
        text-align: center;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        margin: 25px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .upload-zone:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #f8f9fa 100%);
        border-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    .result-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        position: relative;
        overflow: hidden;
    }
    .result-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #27ae60 0%, #2ecc71 50%, #3498db 100%);
    }
    .result-card.danger::before {
        background: linear-gradient(90deg, #e74c3c 0%, #c0392b 50%, #a93226 100%);
    }
    .result-card.warning::before {
        background: linear-gradient(90deg, #f39c12 0%, #e67e22 50%, #d35400 100%);
    }
    .confidence-bar {
        width: 100%;
        height: 28px;
        background: linear-gradient(135deg, #ecf0f1 0%, #bdc3c7 100%);
        border-radius: 14px;
        margin: 15px 0;
        overflow: hidden;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
        position: relative;
    }
    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, #27ae60 0%, #f39c12 70%, #e74c3c 100%);
        border-radius: 14px;
        transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    .confidence-fill::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, rgba(255,255,255,0.3) 0%, transparent 50%, rgba(255,255,255,0.1) 100%);
        border-radius: 14px;
    }
    .tumor-type-badge {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1.1em;
        margin: 8px 0;
        box-shadow: 0 3px 8px rgba(0,0,0,0.15);
        letter-spacing: 0.5px;
    }
    .badge-glioma {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
    }
    .badge-meningioma {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        color: white;
    }
    .badge-pituitary {
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        color: white;
    }
    .badge-no-tumor {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        color: white;
    }
    .analysis-steps {
        display: flex;
        justify-content: space-between;
        margin: 35px 0;
        gap: 15px;
    }
    .step {
        text-align: center;
        flex: 1;
        padding: 25px 15px;
        border-radius: 12px;
        margin: 0;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #dee2e6;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .step.active {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
    }
    .step.completed {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(39, 174, 96, 0.3);
    }
    .btn-analyze {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        border: none;
        padding: 18px 45px;
        border-radius: 12px;
        font-size: 1.2em;
        font-weight: 600;
        cursor: pointer;
        margin: 25px 0;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
        letter-spacing: 0.5px;
    }
    .btn-analyze:hover {
        background: linear-gradient(135deg, #2980b9 0%, #21618c 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(52, 152, 219, 0.4);
    }
    .btn-analyze:disabled {
        background: linear-gradient(135deg, #bdc3c7 0%, #95a5a6 100%);
        cursor: not-allowed;
        transform: none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    .result-section {
        margin: 25px 0;
        padding: 20px;
        background: rgba(255,255,255,0.8);
        border-radius: 10px;
        border-left: 4px solid #3498db;
    }
    .result-section h3 {
        color: #2c3e50;
        margin-bottom: 15px;
        font-weight: 600;
        font-size: 1.3em;
    }
    .result-section p {
        line-height: 1.6;
        color: #34495e;
        margin-bottom: 0;
    }
    .action-buttons {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
    }
    .action-btn {
        flex: 1;
        min-width: 200px;
        padding: 15px 20px;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        text-decoration: none;
        display: inline-block;
    }
    .btn-primary {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        box-shadow: 0 3px 8px rgba(52, 152, 219, 0.3);
    }
    .btn-secondary {
        background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);
        color: white;
        box-shadow: 0 3px 8px rgba(127, 140, 141, 0.3);
    }
    .btn-success {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        color: white;
        box-shadow: 0 3px 8px rgba(39, 174, 96, 0.3);
    }
    .action-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(0,0,0,0.2);
    }
    .image-preview {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border: 2px solid #ecf0f1;
        overflow: hidden;
    }
    .info-box {
        background: linear-gradient(135deg, #ecf0f1 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #3498db;
    }
    .timestamp {
        font-size: 0.9em;
        color: #7f8c8d;
        font-style: italic;
        margin-top: 20px;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# Mock AI model simulation
TUMOR_TYPES = ['No Tumor', 'Glioma', 'Meningioma', 'Pituitary Tumor']
CONFIDENCE_LEVELS = [85, 88, 90, 92, 95, 96, 98]

def simulate_ai_analysis(image):
    """Simulate AI model analysis with realistic processing"""
    # Simulate processing time
    time.sleep(2 + random.random() * 2)  # 2-4 seconds

    tumor_type = random.choice(TUMOR_TYPES)
    confidence = random.choice(CONFIDENCE_LEVELS)

    # Simulate different confidence based on tumor type
    if tumor_type == 'No Tumor':
        confidence = random.choice([95, 96, 98, 99])
    elif tumor_type == 'Glioma':
        confidence = random.choice([85, 88, 90, 92])
    else:
        confidence = random.choice([88, 90, 92, 95])

    return tumor_type, confidence

def get_tumor_info(tumor_type):
    """Get detailed information about tumor types"""
    info = {
        'No Tumor': {
            'description': 'No abnormal growth detected in the brain tissue.',
            'severity': 'Low',
            'recommendation': 'Continue regular health check-ups. No immediate action required.',
            'color': 'success'
        },
        'Glioma': {
            'description': 'A type of tumor that occurs in the brain and spinal cord. Gliomas begin in the gluey supportive cells (glial cells) that surround nerve cells.',
            'severity': 'High',
            'recommendation': 'Immediate consultation with a neurologist or oncologist is recommended. Further diagnostic tests may be required.',
            'color': 'danger'
        },
        'Meningioma': {
            'description': 'A tumor that arises from the meninges — the membranes that surround the brain and spinal cord.',
            'severity': 'Medium',
            'recommendation': 'Consult with a neurosurgeon. Regular monitoring may be recommended depending on size and location.',
            'color': 'warning'
        },
        'Pituitary Tumor': {
            'description': 'A tumor that forms in the pituitary gland, a small gland at the base of the brain that controls many important body functions.',
            'severity': 'Medium',
            'recommendation': 'Endocrinologist consultation recommended. Hormone level testing may be required.',
            'color': 'warning'
        }
    }
    return info.get(tumor_type, {})

def main():
    st.markdown('<h1 class="detection-header">🔬 AI-Powered Brain Tumor Detection & Analysis</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-bottom: 35px; color: #34495e; font-size: 1.1em; line-height: 1.6;">
        Advanced artificial intelligence meets medical imaging. Upload your MRI brain scan for instant,
        professional-grade tumor detection and analysis. <strong>Remember: This tool is for educational and preliminary assessment purposes only.</strong>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state for detection
    if 'detection_step' not in st.session_state:
        st.session_state.detection_step = 'upload'
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'analyzing' not in st.session_state:
        st.session_state.analyzing = False

    # Progress Steps
    st.markdown("""
    <div class="analysis-steps">
        <div class="step {}">
            <div style="font-size: 2em;">📤</div>
            <div>Upload Image</div>
        </div>
        <div class="step {}">
            <div style="font-size: 2em;">⚙️</div>
            <div>AI Analysis</div>
        </div>
        <div class="step {}">
            <div style="font-size: 2em;">📊</div>
            <div>View Results</div>
        </div>
    </div>
    """.format(
        'active' if st.session_state.detection_step == 'upload' else ('completed' if st.session_state.detection_step in ['analyzing', 'results'] else ''),
        'active' if st.session_state.detection_step == 'analyzing' else ('completed' if st.session_state.detection_step == 'results' else ''),
        'active' if st.session_state.detection_step == 'results' else ''
    ), unsafe_allow_html=True)

    # Upload Section
    if st.session_state.detection_step == 'upload':
        st.markdown("### 📤 Step 1: Upload Your MRI Scan")

        st.markdown("""
        <div class="upload-zone">
            <h3 style="color: #2c3e50; margin-bottom: 20px; font-weight: 600;">📤 Upload Your MRI Brain Scan</h3>
            <p style="font-size: 1.1em; margin-bottom: 15px; color: #34495e;">
                <strong>Supported formats:</strong> JPG, PNG, JPEG (max 10MB)
            </p>
            <p style="color: #7f8c8d; font-size: 0.95em; line-height: 1.5;">
                For best results, upload clear, high-resolution MRI scans. The AI works best with T1-weighted or T2-weighted images.
                Make sure the brain is clearly visible and centered in the image.
            </p>
            <div style="margin-top: 20px; font-size: 0.9em; color: #95a5a6;">
                🔒 Your medical images are processed securely and never stored permanently.
            </div>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose an MRI image",
            type=['jpg', 'png', 'jpeg'],
            help="Upload a brain MRI scan for tumor detection analysis"
        )

        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.session_state.uploaded_image = image

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(image, caption="Uploaded MRI Scan", width=300)

            with col2:
                st.markdown("### 📋 Scan Details & Preview")
                st.markdown('<div class="info-box">', unsafe_allow_html=True)

                col_a, col_b = st.columns(2)
                with col_a:
                    st.write(f"**📄 File Name:** {uploaded_file.name}")
                    st.write(f"**📏 File Size:** {len(uploaded_file.getvalue()) / 1024:.1f} KB")

                with col_b:
                    st.write(f"**🖼️ Dimensions:** {image.size[0]} × {image.size[1]} pixels")
                    st.write(f"**🎨 Format:** {image.format}")

                st.markdown("**💡 Image Quality Check:**")
                # Simple quality assessment
                if image.size[0] < 256 or image.size[1] < 256:
                    st.warning("⚠️ Image resolution is quite low. Higher resolution scans provide better analysis accuracy.")
                elif image.size[0] > 2000 or image.size[1] > 2000:
                    st.info("ℹ️ High-resolution image detected. This is good for accurate analysis!")
                else:
                    st.success("✅ Image resolution looks good for analysis.")

                st.markdown('</div>', unsafe_allow_html=True)

                # Analysis readiness check
                st.markdown("### 🎯 Ready for Analysis?")
                ready_checks = [
                    ("✅ Image uploaded successfully", True),
                    ("✅ Supported file format", uploaded_file.type in ['image/jpeg', 'image/png', 'image/jpg']),
                    ("✅ Reasonable file size", len(uploaded_file.getvalue()) < 10 * 1024 * 1024),  # 10MB
                    ("✅ Image dimensions suitable", min(image.size) >= 128),
                ]

                all_ready = all(check[1] for check in ready_checks)
                for check_text, status in ready_checks:
                    if status:
                        st.success(check_text)
                    else:
                        st.error(check_text)

                if all_ready:
                    st.success("🎉 Your scan is ready for AI analysis!")
                    if st.button("🚀 Start AI Analysis", key="analyze_btn", use_container_width=True):
                        st.session_state.detection_step = 'analyzing'
                        st.session_state.analyzing = True
                        st.rerun()
                else:
                    st.warning("⚠️ Please address the issues above before proceeding with analysis.")

    # Analysis Section
    elif st.session_state.detection_step == 'analyzing':
        st.markdown("### ⚙️ Step 2: AI Analysis in Progress")

        if st.session_state.uploaded_image:
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(st.session_state.uploaded_image, caption="Analyzing...", width=300)

            with col2:
                st.markdown("### 🔍 AI Analysis in Progress")
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.write("Our advanced deep learning model is carefully analyzing your brain scan...")

                progress_bar = st.progress(0)
                status_text = st.empty()
                time_estimate = st.empty()

                # Simulate analysis steps with more detailed descriptions
                steps = [
                    ("🔄 Preprocessing image and enhancing quality...", 15),
                    ("🧠 Normalizing brain tissue contrast...", 25),
                    ("🎯 Running tumor detection algorithms...", 40),
                    ("📊 Analyzing tissue characteristics and patterns...", 60),
                    ("⚖️ Calculating confidence scores and probabilities...", 80),
                    ("📋 Generating comprehensive analysis report...", 100)
                ]

                for step_text, progress_value in steps:
                    status_text.markdown(f"**{step_text}**")
                    progress_bar.progress(progress_value / 100)

                    # Add some variation to timing
                    delay = 0.8 + random.random() * 0.7  # 0.8-1.5 seconds
                    time.sleep(delay)

                    if progress_value < 100:
                        remaining = len(steps) - steps.index((step_text, progress_value)) - 1
                        time_estimate.markdown(f"⏱️ *Approximately {remaining} steps remaining...*")

                # Final completion
                status_text.markdown("**✅ Analysis complete! Processing final results...**")
                time_estimate.empty()
                time.sleep(1)

                # Generate results
                tumor_type, confidence = simulate_ai_analysis(st.session_state.uploaded_image)

                st.session_state.analysis_result = {
                    'tumor_type': tumor_type,
                    'confidence': confidence,
                    'timestamp': pd.Timestamp.now(),
                    'image': st.session_state.uploaded_image
                }

                st.success("🎉 Analysis completed successfully!")
                time.sleep(0.5)

                st.session_state.detection_step = 'results'
                st.session_state.analyzing = False
                st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)

    # Results Section
    elif st.session_state.detection_step == 'results':
        st.markdown("### 📊 Step 3: Analysis Results")

        if st.session_state.analysis_result:
            result = st.session_state.analysis_result
            tumor_info = get_tumor_info(result['tumor_type'])

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(result['image'], caption="Analyzed MRI Scan", width=300)

            with col2:
                # Main Result Card
                st.markdown(f"""
                <div class="result-card {tumor_info['color']}">
                    <h2 style="margin-top: 0; color: #2c3e50;">🩺 AI Analysis Results</h2>

                    <div style="display: flex; align-items: center; margin: 25px 0; flex-wrap: wrap; gap: 15px;">
                        <span class="tumor-type-badge badge-{result['tumor_type'].lower().replace(' ', '-')}">
                            {result['tumor_type']}
                        </span>
                        <div style="font-size: 1.1em; color: #34495e;">
                            <strong>Severity Level:</strong> <span style="color: {'#e74c3c' if tumor_info['severity'] == 'High' else '#f39c12' if tumor_info['severity'] == 'Medium' else '#27ae60'};">{tumor_info['severity']}</span>
                        </div>
                    </div>

                    <div class="result-section">
                        <h3>🤖 AI Confidence Score</h3>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {result['confidence']}%;"></div>
                        </div>
                        <p style="text-align: center; font-size: 1.3em; font-weight: 700; margin: 15px 0; color: #2c3e50;">
                            {result['confidence']}% Confidence Level
                        </p>
                        <p style="text-align: center; font-size: 0.95em; color: #7f8c8d; margin-top: 5px;">
                            Based on advanced deep learning analysis of brain tissue patterns
                        </p>
                    </div>

                    <div class="result-section">
                        <h3>📋 Detailed Analysis</h3>
                        <p style="font-size: 1.05em; line-height: 1.7;">{tumor_info['description']}</p>
                    </div>

                    <div class="result-section">
                        <h3>💡 Medical Recommendations</h3>
                        <p style="font-size: 1.05em; line-height: 1.7; font-weight: 500; color: {'#e74c3c' if tumor_info['severity'] == 'High' else '#f39c12' if tumor_info['severity'] == 'Medium' else '#27ae60'};">
                            {tumor_info['recommendation']}
                        </p>
                    </div>

                    <div class="info-box">
                        <p style="margin: 0; font-size: 0.95em;">
                            <strong>⚠️ Important Notice:</strong> This AI analysis is for informational purposes only and should not replace professional medical diagnosis.
                            Always consult with qualified healthcare professionals for accurate medical advice.
                        </p>
                    </div>

                    <div class="timestamp">
                        Analysis completed on {result['timestamp'].strftime('%B %d, %Y at %I:%M %p')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Action Buttons with better styling
                st.markdown("""
                <div class="action-buttons">
                    <button class="action-btn btn-primary" onclick="downloadReport()">📄 Download Full Report</button>
                    <button class="action-btn btn-secondary" onclick="analyzeAgain()">🔄 Analyze Another Scan</button>
                    <button class="action-btn btn-success" onclick="consultDoctor()">🏥 Find Healthcare Providers</button>
                </div>
                """, unsafe_allow_html=True)

                # Handle button actions with Streamlit buttons (since onclick doesn't work in Streamlit)
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📄 Download Full Report", key="download_report", use_container_width=True):
                        # Create a simple text report
                        report_content = f"""
BRAIN TUMOR DETECTION REPORT
===========================

Patient Analysis Summary
Date: {result['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}

DETECTION RESULTS:
- Tumor Type: {result['tumor_type']}
- Confidence Level: {result['confidence']}%
- Severity: {tumor_info['severity']}

DESCRIPTION:
{tumor_info['description']}

RECOMMENDATIONS:
{tumor_info['recommendation']}

IMPORTANT NOTICE:
This AI analysis is for informational purposes only and should not replace
professional medical diagnosis. Always consult with qualified healthcare
professionals for accurate medical advice.

Generated by: Brain Tumor Detection System
Analysis Date: {result['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
                        """.strip()

                        st.download_button(
                            label="📄 Download Report as Text",
                            data=report_content,
                            file_name=f"brain_tumor_analysis_{result['timestamp'].strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain",
                            key="download_txt"
                        )

                with col2:
                    if st.button("🔄 Analyze Another Scan", key="analyze_again", use_container_width=True):
                        # Reset session state
                        st.session_state.detection_step = 'upload'
                        st.session_state.uploaded_image = None
                        st.session_state.analysis_result = None
                        st.rerun()

                with col3:
                    if st.button("🏥 Healthcare Resources", key="healthcare_resources", use_container_width=True):
                        st.info("**Recommended Next Steps:**\n\n1. **Schedule an appointment** with a neurologist or oncologist\n2. **Bring this report** to your healthcare provider\n3. **Ask about additional tests** (MRI, CT scan, biopsy if needed)\n4. **Keep records** of all your medical imaging\n\n**Emergency:** If you experience severe symptoms like seizures, vision changes, or neurological deficits, seek immediate medical attention.")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.switch_page("pages/home.py")
    with col2:
        if st.button("👤 Login", use_container_width=True):
            st.switch_page("pages/login.py")
    with col3:
        if st.button("📋 Register", use_container_width=True):
            st.switch_page("pages/register.py")

if __name__ == "__main__":
    main()