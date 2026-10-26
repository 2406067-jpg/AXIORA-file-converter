# themes.py - Styling CSS Glassmorphism AXIORA Converter Suite


def get_axiora_css():
    return """
    <style>
    /* Reset & Base Theme Glassmorphism */
    .stApp {
        background: radial-gradient(circle at 80% -10%, #1e1b4b 0%, #090d16 50%, #030712 100%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Display & Style Streamlit Header for Mobile/Desktop Navigation */
    header[data-testid="stHeader"] { 
        visibility: visible !important;
        background: rgba(9, 13, 22, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    footer { visibility: hidden; }
    
    /* Sidebar Styling UI Glassmorphism */
    section[data-testid="stSidebar"] {
        background: rgba(11, 17, 32, 0.85) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(16px);
    }
    
    /* Custom Brand Header */
    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
    }
    .brand-logo {
        width: 42px;
        height: 42px;
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        font-weight: 900;
        color: #ffffff;
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
    }
    .brand-text {
        font-size: 1.6rem;
        font-weight: 900;
        letter-spacing: 0.5px;
        color: #ffffff;
        margin: 0;
        line-height: 1;
    }
    .brand-subtext {
        font-size: 0.72rem;
        color: #38bdf8;
        letter-spacing: 0.5px;
        font-weight: 600;
    }

    /* Hero Banner */
    .tag-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #60a5fa;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .main-title {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        line-height: 1.2 !important;
        color: #ffffff;
        margin-bottom: 8px;
    }
    .main-title-highlight {
        background: linear-gradient(135deg, #60a5fa 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-description {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* Feature Pills Responsive */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 10px;
        margin-bottom: 25px;
    }
    .feature-pill {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 10px 12px;
        font-size: 0.78rem;
        color: #cbd5e1;
        display: flex;
        align-items: center;
        gap: 8px;
        backdrop-filter: blur(8px);
    }

    /* File Uploader Container Modern Styling */
    section[data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 2px dashed #2563eb !important;
        border-radius: 18px !important;
        padding: 25px !important;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
    }

    /* Custom Action Button Styling */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 14px 24px !important;
        font-size: 1rem !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 25px rgba(37, 99, 235, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(37, 99, 235, 0.6) !important;
    }

    /* Download Button */
    div[data-testid="stDownloadButton"] > button {
        width: 100%;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 14px 24px !important;
        font-size: 1rem !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 25px rgba(16, 185, 129, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stDownloadButton"] > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(16, 185, 129, 0.6) !important;
    }

    /* Custom Streamlit Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(15, 23, 42, 0.7) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #f8fafc !important;
        font-weight: 700 !important;
    }
    .streamlit-expanderContent {
        background: rgba(11, 17, 32, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 0 0 12px 12px !important;
    }

    /* Status Card */
    .status-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 18px;
        margin-top: 15px;
        backdrop-filter: blur(10px);
    }

    /* Info Cards Bottom Grid */
    .info-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 16px;
        margin-top: 10px;
        height: 100%;
        backdrop-filter: blur(8px);
    }
    .info-card-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 4px;
    }
    .info-card-desc {
        font-size: 0.78rem;
        color: #94a3b8;
    }
    </style>
    """