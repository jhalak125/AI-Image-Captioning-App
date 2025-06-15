import streamlit as st
from utils.gemini_api import generate_caption  

st.set_page_config(page_title="PixVerse", page_icon="🧠", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #0e0e0f;
        font-family: 'Segoe UI', sans-serif;
        color: white;
        margin: 0;
        padding: 0;
    }

    .main-container {
        padding-bottom: 40px;  /* space before footer */
    }

    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #bbbbbb;
        opacity: 0.9;
        margin-top: 4em;
        margin-bottom: 1em;
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    .title-text {
        font-size: 3em;
        font-weight: 800;
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .subtext {
        color: #cccccc;
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 2em;
    }

    .stButton > button {
        background-color: #ff004f;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        font-size: 1.05em;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 10px rgba(255, 75, 43, 0.3);
    }

    .stButton > button:hover {
        background-color: #ff3366;
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(255, 75, 43, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.markdown("##")
st.sidebar.image("Logo.png", width=150)
st.sidebar.title("PixVerse")
st.sidebar.markdown("AI Image Captioning App")

st.sidebar.markdown("### 📝 Latest Updates")
st.sidebar.markdown("""
- ✨ New layout with enhanced visuals  
- 🔍 Improved AI caption accuracy 
- ✏️ Caption refinement coming soon  
- 🌐 Multilingual captioning (beta)  
""")

# --- Main Content Container ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Main Title with Logo ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("Logo.png", width=70)
with col2:
    st.markdown("<div class='title-text'>PixVerse</div>", unsafe_allow_html=True)

st.markdown('<div class="subtext">Upload an image and get an intelligent caption using <strong>Google Gemini Vision Pro</strong>.</div>', unsafe_allow_html=True)

# --- Upload and Caption Generation ---
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        with st.spinner("AI is thinking..."):
            caption = generate_caption(uploaded_file)
        st.success("Generated Caption:")
        st.markdown(f"**{caption}**")

# --- Footer ---
st.markdown("""
    </div>
    <div class="footer">
        🚀 Powered by <strong>Gemini Vision Pro</strong> model
    </div>
""", unsafe_allow_html=True)
