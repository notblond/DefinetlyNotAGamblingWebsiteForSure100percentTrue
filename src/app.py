import os
import sys
import streamlit as st

# Ensure `src` directory is on path so `games` package imports work when running `streamlit run src/app.py`
HERE = os.path.dirname(__file__)
if HERE not in sys.path:
    sys.path.append(HERE)

from games import slots, roulette
from bitcoin_payment import get_wallet_info, check_payment_received

st.set_page_config(page_title="NotGamble Demo", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);}
    .stMetric {background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px; color: white;}
    h1, h2, h3 {color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);}
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 NotGamble — Educational Demo")
st.write("A Streamlit gambling simulation for learning purposes. No real money involved.")

st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🎰 Slots", "🎡 Roulette", "💳 Payment Info"]) 

if page == "🏠 Home":
    st.header("Welcome to NotGamble")
    st.write("""
    This is an **educational demo** showing a simple gambling-style game interface.
    
    **Features:**
    - 🎰 Slot machine game
    - 🎡 Roulette game
    - 💰 Balance tracking (starts at $1,000)
    - ❌ Negative balance protection — you can't play if balance is negative
    - 💳 Bitcoin payment verification (for account reloads)
    
    **How to play:**
    1. Choose a game from the sidebar
    2. Place a bet
    3. Click SPIN to play
    4. Watch your balance change!
    
    ⚠️ **Important:** This is for educational purposes only. No real money is involved.
    """)

    # small CSS animation spinner
    st.markdown(
        """
        <style>
        .spin {width:80px;height:80px;border:6px solid rgba(255,255,255,0.3);border-top-color:#fff;border-radius:50%;animation:spin 1s linear infinite;margin:30px auto}
        @keyframes spin {to {transform: rotate(360deg);}}
        </style>
        <div class="spin"></div>
        """,
        unsafe_allow_html=True,
    )
    st.info("👈 Use the sidebar to pick a game!")

elif page == "🎰 Slots":
    slots.run()

elif page == "🎡 Roulette":
    roulette.run()

elif page == "💳 Payment Info":
    st.header("💳 Payment Verification (Educational)")
    st.write("""
    This feature demonstrates how a real app could verify Bitcoin payments.
    In a real scenario, students would send 0.0001 BTC to get bonus points or reload their balance.
    """)
    
    wallet_info = get_wallet_info()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📬 Wallet Address")
        st.code(wallet_info['address'], language='')
        st.write(f"**Required Payment:** {wallet_info['required_btc']} BTC")
        st.write(f"**= {wallet_info['required_satoshis']} Satoshis**")
    
    with col2:
        st.subheader("✅ Payment Status")
        if st.button("🔍 Check Payment Status"):
            with st.spinner("Checking blockchain..."):
                payment_received = check_payment_received()
                if payment_received:
                    st.success("✅ Payment received! Balance reloaded to $1,000.")
                else:
                    st.warning("⏳ No payment detected yet. Send 0.0001 BTC to the wallet address above.")
    
    st.divider()
    st.info("""
    **Note:** This uses the Blockchain.com API to check the wallet balance.
    It's free and requires no authentication. 
    This is purely for educational demonstration.
    """)

