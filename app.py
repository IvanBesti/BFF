import streamlit as st
import requests
import time

# Page config
st.set_page_config(
    page_title="Message for You ❤️",
    page_icon="❤️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff6b6b, #ffd93d);
    }
    .stButton>button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 18px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
    }
    .message-text {
        font-size: 28px;
        color: #ff4b4b;
        text-align: center;
        padding: 20px;
        margin: 20px 0;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    .youtube-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%;
        margin-bottom: 20px;
        opacity: 0;
        transition: opacity 1s ease-in-out;
    }
    .youtube-container.show {
        opacity: 1;
    }
    .youtube-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Floating Hearts Animation */
    .hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .heart {
        position: absolute;
        font-size: 30px;
        color: #ff69b4;
        animation: float-up 4s ease-in-out infinite;
        opacity: 0;
    }
    
    .heart:nth-child(1) { left: 10%; animation-delay: 0s; }
    .heart:nth-child(2) { left: 20%; animation-delay: 0.5s; }
    .heart:nth-child(3) { left: 30%; animation-delay: 1s; }
    .heart:nth-child(4) { left: 40%; animation-delay: 1.5s; }
    .heart:nth-child(5) { left: 50%; animation-delay: 2s; }
    .heart:nth-child(6) { left: 60%; animation-delay: 2.5s; }
    .heart:nth-child(7) { left: 70%; animation-delay: 3s; }
    .heart:nth-child(8) { left: 80%; animation-delay: 3.5s; }
    .heart:nth-child(9) { left: 90%; animation-delay: 4s; }
    .heart:nth-child(10) { left: 15%; animation-delay: 4.5s; }
    
    @keyframes float-up {
        0% {
            opacity: 0;
            transform: translateY(100vh) rotate(0deg);
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translateY(-100px) rotate(360deg);
        }
    }
    
    .hearts.show {
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# Create container for centered content
container = st.container()

# State for tracking button click
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

with container:
    # Add some space at the top
    st.write("")
    st.write("")
    
    # Display message with typing effect
    message = "Selamat kamu telah menjadi pacar Ivan"
    st.markdown(f'<p class="message-text">{message}</p>', unsafe_allow_html=True)
    
    # Add a cute button
    if st.button("❤️ Click Me ❤️"):
        st.session_state.button_clicked = True
        st.balloons()
        st.snow()
        st.rerun()
    
    # Display floating hearts animation when button is clicked
    if st.session_state.button_clicked:
        st.markdown("""
            <div class="hearts show">
                <div class="heart">💖</div>
                <div class="heart">💕</div>
                <div class="heart">💗</div>
                <div class="heart">💓</div>
                <div class="heart">💝</div>
                <div class="heart">💞</div>
                <div class="heart">💟</div>
                <div class="heart">❤️</div>
                <div class="heart">🧡</div>
                <div class="heart">💛</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Display YouTube Video only after button click
    if st.session_state.button_clicked:
        youtube_video_id = "QGlC-9OELAo"  # Daniel Caesar - Get You
        youtube_embed = f"""
            <div class="youtube-container show">
                <iframe
                    src="https://www.youtube.com/embed/{youtube_video_id}?autoplay=1&mute=0&controls=1&showinfo=0&rel=0&iv_load_policy=3&playsinline=1&start=46"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowfullscreen
                ></iframe>
            </div>
        """
        st.markdown(youtube_embed, unsafe_allow_html=True) 