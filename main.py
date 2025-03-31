import streamlit as st
import random
from streamlit.components.v1 import html

# List of Eid Mubarak wishes
greetings = [
    "Eid Mubarak! May your heart and home be filled with joy and blessings.",
    "Wishing you a joyous Eid filled with love and prosperity!",
    "May Allah's blessings be with you today and always. Eid Mubarak!",
    "Eid Mubarak! May this special day bring peace, happiness, and prosperity to everyone.",
    "May the magic of Eid bring lots of happiness and fill your life with peace and joy. Eid Mubarak!",
    "On this blessed occasion, may Allah accept your good deeds and prayers. Eid Mubarak!",
    "Wishing you and your family a very happy Eid filled with moments of joy and togetherness.",
    "May the divine blessings of Allah bring you hope, faith, and joy on Eid and forever. Eid Mubarak!"
]

# CSS for animations and styling
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    body {
        font-family: 'Amiri', serif;
        background-color: #f8f3e6;
    }
    
    .eid-title {
        font-family: 'Amiri', serif;
        font-size: 3rem;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #e6c229, 0 0 20px #e6c229;
        }
        to {
            text-shadow: 0 0 10px #fff, 0 0 20px #ffd700, 0 0 30px #ffd700, 0 0 40px #ffd700;
        }
    }
    
    .greeting-card {
        background: linear-gradient(135deg, #f5f5dc 0%, #fff9e6 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #d4af37;
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .eid-button-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #f9d423 100%);
        color: white;
        font-family: 'Amiri', serif;
        font-size: 1.2rem;
        padding: 12px 30px;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
        transition: all 0.3s ease;
        margin: 0 auto;
        display: block;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6);
        background: linear-gradient(135deg, #f9d423 0%, #d4af37 100%);
        color: white !important;
    }
    
    .stButton>button:active {
        transform: translateY(1px);
    }
    
    .decoration {
        text-align: center;
        font-size: 2rem;
        margin: 0.5rem 0;
        color: #d4af37;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #666;
        font-size: 0.9rem;
    }
</style>
"""

# App UI
st.set_page_config(
    page_title="Eid Mubarak Greeting App", 
    page_icon="🌙", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title with decorative elements
st.markdown("""
    <div class="decoration">🌙 ⋆ * ⋆ ✨ ⋆ * ⋆ 🌙</div>
    <h1 class="eid-title">Eid Mubarak</h1>
    <div class="decoration">✨ ⋆ * ⋆ 🌙 ⋆ * ⋆ ✨</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem; color: #555;">
        <p style="font-size: 1.2rem;">Click the button below to receive a special Eid greeting</p>
    </div>
""", unsafe_allow_html=True)

# Center-aligned button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Get Eid Mubarak Wish", key="eid_button"):
        selected_greeting = random.choice(greetings)
        st.markdown(f"""
            <div class="greeting-card">
                <p style="font-size: 1.4rem; text-align: center; color: #333; line-height: 1.6;">
                    {selected_greeting}
                </p>
                <div style="text-align: center; margin-top: 1rem; font-size: 2rem;">✨🌙✨</div>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Wishing you and your family a blessed Eid al-Fitr</p>
        <p>May this Eid bring peace, happiness, and prosperity to all</p>
    </div>
""", unsafe_allow_html=True)