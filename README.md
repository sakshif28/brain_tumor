# Brain Tumor Detection System

A professional, healthcare-grade frontend interface for AI-powered brain tumor detection using MRI scans, built with Python and Streamlit.

## Features

### User Roles
- **Patient**: Register, login, upload MRI scans, view results, access scan history and reports
- **Admin (Medical Staff)**: Login to separate dashboard, review all patient scans, monitor system activity, add diagnostic notes

### Patient Features
- User registration and authentication
- MRI image upload (JPG, PNG, JPEG)
- Real-time AI tumor detection simulation
- Scan history with results
- Diagnostic reports
- Profile management

### Admin Features
- Secure admin login
- Dashboard with system statistics
- Patient management overview
- Scan review with doctor notes
- Tumor type distribution charts
- Recent activity monitoring

### UI Design
- Medical-themed professional design
- Clean, minimal interface
- Color-coded results (Green: No Tumor, Red: Tumor Detected)
- Responsive layout
- Accessibility-focused

## Technology Stack

- **Frontend**: Streamlit
- **Language**: Python 3.11
- **Libraries**: 
  - streamlit
  - pandas
  - pillow (PIL)
  - numpy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd brain_tumor
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
venv\Scripts\activate  # Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Choose your role:
   - **Patient**: Register/Login → Upload MRI → View Results
   - **Admin**: Login with admin credentials → Review scans

## Project Structure

```
brain_tumor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created)
```

## Mock Data & Simulation

Since the ML model is not implemented, the system uses simulated predictions:
- Tumor types: No Tumor, Glioma, Meningioma, Pituitary Tumor
- Confidence levels: 85%, 90%, 92%, 95%, 98%
- Results are randomly generated for demonstration

## Future Integration

The UI is designed for easy API integration:
- Replace `simulate_prediction()` with actual ML model calls
- Add API endpoints for authentication
- Implement real database storage
- Add DICOM file support
- Integrate with medical imaging APIs

## Security Features

- Role-based access control
- Separate admin authentication
- Session state management
- Input validation
- Secure file upload handling

## Medical Compliance

- HIPAA-inspired design principles
- Professional medical terminology
- Clear result presentation
- Audit trail capabilities (simulated)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes. Consult medical professionals for actual diagnostic use.