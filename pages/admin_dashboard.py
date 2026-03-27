import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="Brain Tumor Detection - Admin",
    page_icon="👨‍⚕️",
    layout="wide"
)

# Custom CSS for admin dashboard
st.markdown("""
<style>
    .admin-header {
        color: #dc3545;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .admin-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #dc3545;
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
    .alert-card {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    .patient-table {
        background-color: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .status-badge {
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        font-weight: bold;
    }
    .status-normal {
        background-color: #d4edda;
        color: #155724;
    }
    .status-warning {
        background-color: #fff3cd;
        color: #856404;
    }
    .status-danger {
        background-color: #f8d7da;
        color: #721c24;
    }
    .sidebar-admin {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .nav-admin {
        display: block;
        padding: 10px 15px;
        margin: 5px 0;
        text-decoration: none;
        color: #333;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .nav-admin:hover {
        background-color: #dc3545;
        color: white;
    }
    .nav-admin.active {
        background-color: #dc3545;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def generate_mock_admin_data():
    """Generate mock data for admin dashboard"""
    # Mock patients
    patients = []
    names = ["John Smith", "Sarah Johnson", "Michael Brown", "Emily Davis", "David Wilson",
             "Lisa Anderson", "Robert Taylor", "Jennifer Martinez", "James Garcia", "Linda Rodriguez"]

    for i, name in enumerate(names):
        patient = {
            'id': f'P{i+1:03d}',
            'name': name,
            'email': f'{name.lower().replace(" ", ".")}@example.com',
            'age': random.randint(25, 75),
            'gender': random.choice(['Male', 'Female']),
            'total_scans': random.randint(0, 8),
            'last_scan': pd.Timestamp.now() - pd.Timedelta(days=random.randint(0, 30)),
            'status': random.choice(['Active', 'Inactive'])
        }
        patients.append(patient)

    # Mock scans
    scans = []
    tumor_types = ['No Tumor', 'Glioma', 'Meningioma', 'Pituitary Tumor']

    for _ in range(50):
        scan = {
            'patient_id': f'P{random.randint(1, 10):03d}',
            'patient_name': random.choice(names),
            'date': pd.Timestamp.now() - pd.Timedelta(days=random.randint(0, 30)),
            'tumor_type': random.choice(tumor_types),
            'confidence': random.randint(85, 98),
            'status': 'completed'
        }
        scans.append(scan)

    return patients, scans

def main():
    # Check if admin is logged in
    if not st.session_state.get('logged_in', False) or st.session_state.get('user_role') != 'admin':
        st.error("Access denied. Admin login required.")
        st.switch_page("pages/login.py")
        return

    # Generate mock data if not exists
    if 'admin_patients' not in st.session_state:
        patients, scans = generate_mock_admin_data()
        st.session_state.admin_patients = patients
        st.session_state.admin_scans = scans
    else:
        patients = st.session_state.admin_patients
        scans = st.session_state.admin_scans

    # Sidebar Navigation
    with st.sidebar:
        st.markdown('<div class="sidebar-admin">', unsafe_allow_html=True)
        st.markdown("### 👨‍⚕️ Admin Panel")

        if st.button("📊 Dashboard", key="admin_nav_dashboard", use_container_width=True):
            st.session_state.admin_page = "dashboard"
            st.rerun()
        if st.button("👥 Patient Mgmt", key="admin_nav_patients", use_container_width=True):
            st.session_state.admin_page = "patients"
            st.rerun()
        if st.button("🔍 Scan Review", key="admin_nav_scans", use_container_width=True):
            st.session_state.admin_page = "scans"
            st.rerun()
        if st.button("📈 Analytics", key="admin_nav_analytics", use_container_width=True):
            st.session_state.admin_page = "analytics"
            st.rerun()

        st.markdown("---")
        if st.button("🚪 Logout", key="admin_nav_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.success("Logged out successfully")
            st.switch_page("pages/home.py")

        st.markdown('</div>', unsafe_allow_html=True)

    # Main Content
    current_page = st.session_state.get('admin_page', 'dashboard')

    if current_page == "dashboard":
        show_admin_main_dashboard(patients, scans)
    elif current_page == "patients":
        show_patient_management(patients)
    elif current_page == "scans":
        show_scan_review(scans)
    elif current_page == "analytics":
        show_analytics(patients, scans)

def show_admin_main_dashboard(patients, scans):
    st.markdown('<h1 class="admin-header">👨‍⚕️ Admin Dashboard</h1>', unsafe_allow_html=True)

    # Alert for urgent cases
    urgent_cases = [s for s in scans if s['tumor_type'] != 'No Tumor' and s['confidence'] > 90]
    if urgent_cases:
        st.markdown(f"""
        <div class="alert-card">
            <strong>⚠️ Urgent Attention Required:</strong> {len(urgent_cases)} high-confidence tumor detections need review
        </div>
        """, unsafe_allow_html=True)

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(patients)}</div>
            <div class="metric-label">Total Patients</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(scans)}</div>
            <div class="metric-label">Total Scans</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        tumor_scans = [s for s in scans if s['tumor_type'] != 'No Tumor']
        detection_rate = len(tumor_scans) / len(scans) * 100 if scans else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{detection_rate:.1f}%</div>
            <div class="metric-label">Detection Rate</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        avg_confidence = sum(s['confidence'] for s in scans) / len(scans) if scans else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{avg_confidence:.1f}%</div>
            <div class="metric-label">Avg Confidence</div>
        </div>
        """, unsafe_allow_html=True)

    # Recent Activity
    st.markdown("### 🕒 Recent Scans")
    recent_scans = sorted(scans, key=lambda x: x['date'], reverse=True)[:10]

    for scan in recent_scans:
        status_class = 'status-normal' if scan['tumor_type'] == 'No Tumor' else 'status-danger'
        st.markdown(f"""
        <div class="admin-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{scan['patient_name']}</strong> - {scan['date'].strftime('%Y-%m-%d %H:%M')}<br>
                    <span class="status-badge {status_class}">{scan['tumor_type']}</span>
                    <span style="margin-left: 10px; color: #666;">{scan['confidence']}% confidence</span>
                </div>
                <div>
                    {scan['status'].title()}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_patient_management(patients):
    st.markdown('<h1 class="admin-header">👥 Patient Management</h1>', unsafe_allow_html=True)

    # Search and Filter
    col1, col2, col3 = st.columns(3)
    with col1:
        search_name = st.text_input("Search by name", placeholder="Enter patient name")
    with col2:
        filter_status = st.selectbox("Filter by status", ["All", "Active", "Inactive"])
    with col3:
        sort_by = st.selectbox("Sort by", ["Name", "Last Scan", "Total Scans"])

    # Apply filters
    filtered_patients = patients
    if search_name:
        filtered_patients = [p for p in patients if search_name.lower() in p['name'].lower()]
    if filter_status != "All":
        filtered_patients = [p for p in filtered_patients if p['status'] == filter_status]

    # Apply sorting
    if sort_by == "Name":
        filtered_patients = sorted(filtered_patients, key=lambda x: x['name'])
    elif sort_by == "Last Scan":
        filtered_patients = sorted(filtered_patients, key=lambda x: x['last_scan'], reverse=True)
    elif sort_by == "Total Scans":
        filtered_patients = sorted(filtered_patients, key=lambda x: x['total_scans'], reverse=True)

    # Display patients
    st.markdown(f"### Showing {len(filtered_patients)} patients")

    for patient in filtered_patients:
        status_class = 'status-normal' if patient['status'] == 'Active' else 'status-warning'
        st.markdown(f"""
        <div class="admin-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{patient['name']}</strong> ({patient['id']})<br>
                    <span style="color: #666;">{patient['email']} • Age: {patient['age']} • {patient['gender']}</span><br>
                    <span class="status-badge {status_class}">{patient['status']}</span>
                    <span style="margin-left: 10px; color: #666;">{patient['total_scans']} scans • Last: {patient['last_scan'].strftime('%Y-%m-%d')}</span>
                </div>
                <div>
                    <button style="background-color: #0066cc; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">View Details</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_scan_review(scans):
    st.markdown('<h1 class="admin-header">🔍 Scan Review</h1>', unsafe_allow_html=True)

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_tumor = st.selectbox("Filter by tumor type", ["All", "No Tumor", "Glioma", "Meningioma", "Pituitary Tumor"])
    with col2:
        filter_confidence = st.slider("Min confidence", 0, 100, 0)
    with col3:
        sort_by = st.selectbox("Sort by", ["Date (Newest)", "Date (Oldest)", "Confidence (High)", "Confidence (Low)"])

    # Apply filters
    filtered_scans = scans
    if filter_tumor != "All":
        filtered_scans = [s for s in scans if s['tumor_type'] == filter_tumor]
    filtered_scans = [s for s in filtered_scans if s['confidence'] >= filter_confidence]

    # Apply sorting
    if sort_by == "Date (Newest)":
        filtered_scans = sorted(filtered_scans, key=lambda x: x['date'], reverse=True)
    elif sort_by == "Date (Oldest)":
        filtered_scans = sorted(filtered_scans, key=lambda x: x['date'])
    elif sort_by == "Confidence (High)":
        filtered_scans = sorted(filtered_scans, key=lambda x: x['confidence'], reverse=True)
    elif sort_by == "Confidence (Low)":
        filtered_scans = sorted(filtered_scans, key=lambda x: x['confidence'])

    st.markdown(f"### Reviewing {len(filtered_scans)} scans")

    for scan in filtered_scans:
        status_class = 'status-normal' if scan['tumor_type'] == 'No Tumor' else 'status-danger'
        st.markdown(f"""
        <div class="admin-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{scan['patient_name']}</strong> - {scan['date'].strftime('%Y-%m-%d %H:%M')}<br>
                    <span class="status-badge {status_class}">{scan['tumor_type']}</span>
                    <span style="margin-left: 10px; color: #666;">{scan['confidence']}% confidence</span>
                </div>
                <div>
                    <button style="background-color: #28a745; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin-right: 5px;">Approve</button>
                    <button style="background-color: #ffc107; color: black; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin-right: 5px;">Flag</button>
                    <button style="background-color: #dc3545; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer;">Review</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_analytics(patients, scans):
    st.markdown('<h1 class="admin-header">📈 Analytics & Insights</h1>', unsafe_allow_html=True)

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Tumor Type Distribution")
        if scans:
            tumor_counts = pd.Series([s['tumor_type'] for s in scans]).value_counts()
            st.bar_chart(tumor_counts)

    with col2:
        st.markdown("### Confidence Score Distribution")
        if scans:
            confidence_data = pd.DataFrame({
                'Confidence': [s['confidence'] for s in scans]
            })
            st.histogram(confidence_data)

    # Time series
    st.markdown("### Scan Activity Over Time")
    if scans:
        # Group by date
        scan_dates = [s['date'].date() for s in scans]
        date_counts = pd.Series(scan_dates).value_counts().sort_index()
        st.line_chart(date_counts)

    # Key metrics
    st.markdown("### Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        active_patients = len([p for p in patients if p['status'] == 'Active'])
        st.metric("Active Patients", active_patients)

    with col2:
        avg_scans_per_patient = len(scans) / len(patients) if patients else 0
        st.metric("Avg Scans/Patient", f"{avg_scans_per_patient:.1f}")

    with col3:
        high_confidence = len([s for s in scans if s['confidence'] >= 95])
        st.metric("High Confidence Scans", high_confidence)

    with col4:
        recent_scans = len([s for s in scans if (pd.Timestamp.now() - s['date']).days <= 7])
        st.metric("Scans This Week", recent_scans)

if __name__ == "__main__":
    main()