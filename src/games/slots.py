import streamlit as st
import random

SYMBOLS = ['🍒','🍋','🍊','⭐','7']

def spin_reels():
    return [random.choice(SYMBOLS) for _ in range(3)]

def payout(reels, bet):
    if reels.count(reels[0]) == 3:
        if reels[0] == '7':
            return bet * 50
        return bet * 5
    if reels.count(reels[0]) == 2:
        return bet * 2
    return 0


def run():
    st.header('🎰 Slots')
    
    if 'balance' not in st.session_state:
        st.session_state.balance = 1000
    
    # Display balance with styling
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💰 Balance", f"${st.session_state.balance:.2f}")
    with col2:
        if st.session_state.balance < 0:
            st.metric("Status", "❌ NEGATIVE", delta=None)
        else:
            st.metric("Status", "✅ OK", delta=None)
    
    st.divider()
    
    # Bet input
    bet = st.number_input('Bet amount', min_value=1, value=10, step=1)
    
    # Check balance before allowing spin
    if st.session_state.balance <= 0:
        st.error('❌ You cannot play with a negative or zero balance. Please reload your account.')
        return
    
    if bet > st.session_state.balance:
        st.warning(f'⚠️ Bet ({bet}) exceeds balance ({st.session_state.balance:.2f})')
        return
    
    reels = ['?', '?', '?']
    
    # Spin button with styling
    spin_col1, spin_col2, spin_col3 = st.columns(3)
    with spin_col2:
        if st.button('🎬 SPIN', use_container_width=True, type='primary'):
            with st.spinner('Spinning reels...'):
                import time
                time.sleep(1)  # Animation delay
                reels = spin_reels()
                win = payout(reels, bet)
                st.session_state.balance += (win - bet)
                
                # Display result with colors
                if win > 0:
                    st.success(f'🎉 You spun: **{" ".join(reels)}** — Won: **${win:.2f}** — New Balance: **${st.session_state.balance:.2f}**')
                else:
                    st.info(f'😞 You spun: {" ".join(reels)} — Lost ${bet:.2f} — New Balance: ${st.session_state.balance:.2f}')
    
    st.divider()
    
    # Display reels with large font
    reel_display = ' '.join(reels)
    st.markdown(f'<div style="text-align:center; font-size:80px; font-weight:bold; padding:20px; background:#f0f0f0; border-radius:10px;">{reel_display}</div>', unsafe_allow_html=True)
