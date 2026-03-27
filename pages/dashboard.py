import streamlit as st
import pandas as pd
import random
from PIL import Image

st.set_page_config(
    page_title="Brain Tumor Detection - Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for dashboard
st.markdown("""
<style>
    .dashboard-header {
        color: #0066cc;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .welcome-card {
        background: linear-gradient(135deg, #0066cc 0%, #008080 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
    }
    .metric-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px;
        border-left: 4px solid #0066cc;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #0066cc;
        margin: 10px 0;
    }
    .metric-label {
        color: #666;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .quick-action-card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid transparent;
    }
    .quick-action-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border-color: #0066cc;
    }
    .scan-history-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #28a745;
    }
    .scan-history-card.warning {
        border-left-color: #ffc107;
    }
    .scan-history-card.danger {
        border-left-color: #dc3545;
    }
    .sidebar-nav {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .nav-item {
        display: block;
        padding: 10px 15px;
        margin: 5px 0;
        text-decoration: none;
        color: #333;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .nav-item:hover {
        background-color: #0066cc;
        color: white;
    }
    .nav-item.active {
        background-color: #0066cc;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def get_risk_color(tumor_type):
    if tumor_type == 'No Tumor':
        return 'success'
    else:
        return 'danger'

def generate_mock_scan_history():
    """Generate mock scan history for demo"""
    tumor_types = ['No Tumor', 'Glioma', 'Meningioma', 'Pituitary Tumor']
    dates = pd.date_range(end=pd.Timestamp.now(), periods=5, freq='D')

    history = []
    for i, date in enumerate(dates):
        tumor_type = random.choice(tumor_types)
        confidence = random.randint(85, 98)
        history.append({
            'date': date.strftime('%Y-%m-%d %H:%M'),
            'tumor_type': tumor_type,
            'confidence': confidence,
            'status': 'completed'
        })
    return history

def main():
    # Check if user is logged in
    if not st.session_state.get('logged_in', False) or st.session_state.get('user_role') != 'patient':
        st.error("Please login to access your dashboard")
        st.switch_page("pages/login.py")
        return

    user_data = st.session_state.get('user_data', {})
    scan_history = st.session_state.get('scan_history', [])

    # If no scan history, generate mock data
    if not scan_history:
        scan_history = generate_mock_scan_history()
        st.session_state.scan_history = scan_history

    # Sidebar Navigation
    with st.sidebar:
        st.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
        st.markdown("### 🧠 Navigation")

        if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
            st.session_state.dashboard_page = "dashboard"
            st.rerun()
        if st.button("📤 Upload MRI", key="nav_upload", use_container_width=True):
            st.session_state.dashboard_page = "upload"
            st.rerun()
        if st.button("📋 Scan History", key="nav_history", use_container_width=True):
            st.session_state.dashboard_page = "history"
            st.rerun()
        if st.button("📄 Reports", key="nav_reports", use_container_width=True):
            st.session_state.dashboard_page = "reports"
            st.rerun()
        if st.button("👤 Profile", key="nav_profile", use_container_width=True):
            st.session_state.dashboard_page = "profile"
            st.rerun()

        st.markdown("---")
        if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.success("Logged out successfully")
            st.switch_page("pages/home.py")

        st.markdown('</div>', unsafe_allow_html=True)

    # Main Content
    current_page = st.session_state.get('dashboard_page', 'dashboard')

    if current_page == "dashboard":
        show_main_dashboard(user_data, scan_history)
    elif current_page == "upload":
        show_upload_page()
    elif current_page == "history":
        show_history_page(scan_history)
    elif current_page == "reports":
        show_reports_page(scan_history)
    elif current_page == "profile":
        show_profile_page(user_data)

def show_main_dashboard(user_data, scan_history):
    st.markdown('<h1 class="dashboard-header">📊 Patient Dashboard</h1>', unsafe_allow_html=True)

    # Welcome Card
    st.markdown(f"""
    <div class="welcome-card">
        <h2>Welcome back, {user_data.get('name', 'Patient')}!</h2>
        <p>Access your brain tumor detection results and manage your medical records</p>
    </div>
    """, unsafe_allow_html=True)

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(scan_history)}</div>
            <div class="metric-label">Total Scans</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        latest_scan = scan_history[0] if scan_history else None
        status = latest_scan['tumor_type'] if latest_scan else "No scans"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{status[:10]}</div>
            <div class="metric-label">Last Result</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        healthy_scans = len([s for s in scan_history if s['tumor_type'] == 'No Tumor'])
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{healthy_scans}</div>
            <div class="metric-label">Healthy Scans</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        avg_confidence = sum(s['confidence'] for s in scan_history) / len(scan_history) if scan_history else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{avg_confidence:.0f}%</div>
            <div class="metric-label">Avg Confidence</div>
        </div>
        """, unsafe_allow_html=True)

    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="quick-action-card">', unsafe_allow_html=True)
        st.markdown("### 🔬 New Scan")
        st.write("Upload a new MRI for analysis")
        if st.button("Start Analysis", key="quick_scan"):
            st.session_state.dashboard_page = "upload"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="quick-action-card">', unsafe_allow_html=True)
        st.markdown("### 📋 View History")
        st.write("Review your scan history")
        if st.button("View History", key="quick_history"):
            st.session_state.dashboard_page = "history"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="quick-action-card">', unsafe_allow_html=True)
        st.markdown("### 📄 Get Report")
        st.write("Download your latest report")
        if st.button("Download Report", key="quick_report"):
            st.session_state.dashboard_page = "reports"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Recent Activity
    st.markdown("### 🕒 Recent Activity")
    if scan_history:
        for scan in scan_history[:3]:
            color_class = get_risk_color(scan['tumor_type'])
            st.markdown(f"""
            <div class="scan-history-card {color_class}">
                <strong>{scan['date']}</strong> - {scan['tumor_type']} ({scan['confidence']}% confidence)
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No scan history available. Upload your first MRI scan!")

def show_upload_page():
    st.markdown('<h1 class="dashboard-header">📤 Upload MRI Scan</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e7f3ff; border: 1px solid #b3d7ff; border-radius: 10px; padding: 20px; margin: 20px 0;">
        <h4 style="color: #0066cc; margin-top: 0;">📋 Upload Instructions</h4>
        <ul>
            <li>Upload clear, high-resolution MRI brain scans</li>
            <li>Supported formats: JPG, PNG, JPEG</li>
            <li>Maximum file size: 10MB</li>
            <li>Analysis typically takes 2-4 seconds</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose an MRI image",
        type=['jpg', 'png', 'jpeg'],
        help="Select a brain MRI scan for tumor detection analysis"
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(image, caption="Uploaded MRI", width=300)

        with col2:
            st.markdown("### 📋 Image Details")
            st.write(f"**File Name:** {uploaded_file.name}")
            st.write(f"**File Size:** {len(uploaded_file.getvalue()) / 1024:.1f} KB")
            st.write(f"**Dimensions:** {image.size[0]} x {image.size[1]} pixels")

            if st.button("🔬 Start AI Analysis", use_container_width=True):
                with st.spinner("Analyzing MRI scan..."):
                    import time
                    time.sleep(2)

                    # Mock analysis
                    tumor_types = ['No Tumor', 'Glioma', 'Meningioma', 'Pituitary Tumor']
                    tumor_type = random.choice(tumor_types)
                    confidence = random.randint(85, 98)

                    # Save to history
                    scan_data = {
                        'date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M'),
                        'tumor_type': tumor_type,
                        'confidence': confidence,
                        'status': 'completed'
                    }
                    st.session_state.scan_history.insert(0, scan_data)

                    st.success("Analysis completed!")
                    st.rerun()

def show_history_page(scan_history):
    st.markdown('<h1 class="dashboard-header">📋 Scan History</h1>', unsafe_allow_html=True)

    if not scan_history:
        st.info("No scan history available. Upload your first MRI scan!")
        return

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        filter_status = st.selectbox("Filter by Result", ["All", "No Tumor", "Glioma", "Meningioma", "Pituitary Tumor"])
    with col2:
        sort_by = st.selectbox("Sort by", ["Date (Newest)", "Date (Oldest)", "Confidence (High)", "Confidence (Low)"])

    # Apply filters
    filtered_history = scan_history
    if filter_status != "All":
        filtered_history = [s for s in scan_history if s['tumor_type'] == filter_status]

    # Apply sorting
    if sort_by == "Date (Newest)":
        filtered_history = sorted(filtered_history, key=lambda x: x['date'], reverse=True)
    elif sort_by == "Date (Oldest)":
        filtered_history = sorted(filtered_history, key=lambda x: x['date'])
    elif sort_by == "Confidence (High)":
        filtered_history = sorted(filtered_history, key=lambda x: x['confidence'], reverse=True)
    elif sort_by == "Confidence (Low)":
        filtered_history = sorted(filtered_history, key=lambda x: x['confidence'])

    # Display history
    for scan in filtered_history:
        color_class = get_risk_color(scan['tumor_type'])
        st.markdown(f"""
        <div class="scan-history-card {color_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{scan['date']}</strong><br>
                    <span style="color: #666;">{scan['tumor_type']} • {scan['confidence']}% confidence</span>
                </div>
                <div>
                    {scan['status'].title()}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_reports_page(scan_history):
    st.markdown('<h1 class="dashboard-header">📄 Medical Reports</h1>', unsafe_allow_html=True)

    if not scan_history:
        st.info("No reports available. Complete your first scan analysis!")
        return

    user_data = st.session_state.get('user_data', {})

    for i, scan in enumerate(scan_history):
        with st.expander(f"Report: {scan['date']} - {scan['tumor_type']}"):
            st.markdown(f"""
            ### 🏥 Brain Tumor Detection Report

            **Patient Information:**
            - Name: {user_data.get('name', 'N/A')}
            - Email: {user_data.get('email', 'N/A')}
            - Age: {user_data.get('age', 'N/A')}
            - Gender: {user_data.get('gender', 'N/A')}

            **Scan Details:**
            - Date: {scan['date']}
            - Analysis Type: AI-Powered Tumor Detection
            - Model Version: v2.1

            **Results:**
            - Tumor Type: {scan['tumor_type']}
            - Confidence Score: {scan['confidence']}%
            - Risk Level: {"Low" if scan['tumor_type'] == "No Tumor" else "High"}

            **Recommendations:**
            - {"Continue regular health monitoring" if scan['tumor_type'] == "No Tumor" else "Consult with a healthcare professional immediately"}
            - Schedule follow-up appointment if needed
            - Keep this report for your medical records

            **Disclaimer:** This AI analysis is for informational purposes only and should not replace professional medical advice.
            """)

            if st.button(f"Download Report {i+1}", key=f"download_{i}"):
                st.success("Report download feature will be available in the full implementation!")

def show_profile_page(user_data):
    st.markdown('<h1 class="dashboard-header">👤 Patient Profile</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
            <div style="font-size: 4em;">👤</div>
            <h3>Patient Profile</h3>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Personal Information")
        st.write(f"**Full Name:** {user_data.get('name', 'N/A')}")
        st.write(f"**Email:** {user_data.get('email', 'N/A')}")
        st.write(f"**Phone:** {user_data.get('phone', 'N/A')}")
        st.write(f"**Age:** {user_data.get('age', 'N/A')}")
        st.write(f"**Gender:** {user_data.get('gender', 'N/A')}")

        if user_data.get('medical_conditions'):
            st.markdown("### Medical Information")
            st.write(f"**Medical Conditions:** {user_data['medical_conditions']}")

        st.markdown("### Account Status")
        st.write("**Account Type:** Patient")
        st.write("**Registration Date:** Today")
        st.write("**Status:** Active")

if __name__ == "__main__":
    main()