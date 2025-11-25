import streamlit as st
import random


def pick_color(n):
    if n == 0:
        return 'green'
    return 'red' if n % 2 == 1 else 'black'


def run():
    st.header('🎡 Roulette')
    
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
    
    # Check balance before allowing play
    if st.session_state.balance <= 0:
        st.error('❌ You cannot play with a negative or zero balance. Please reload your account.')
        return
    
    # Bet type selection
    bet_type = st.radio('Bet on', ['🔢 Number', '🎨 Color'], horizontal=True)
    
    if bet_type == '🔢 Number':
        number = st.number_input('Pick a number (0-36)', min_value=0, max_value=36, value=17)
    else:
        color = st.selectbox('Choose color', ['🔴 Red', '⚫ Black'])
        color = color.split()[1].lower()  # Extract 'red' or 'black'

    bet = st.number_input('Bet amount', min_value=1, value=10, step=1)
    
    if bet > st.session_state.balance:
        st.warning(f'⚠️ Bet ({bet}) exceeds balance ({st.session_state.balance:.2f})')
        return
    
    # Spin button
    spin_col1, spin_col2, spin_col3 = st.columns(3)
    with spin_col2:
        if st.button('🎬 SPIN', use_container_width=True, type='primary'):
            with st.spinner('Spinning the wheel...'):
                import time
                time.sleep(2)  # Animation delay
                result = random.randint(0, 36)
                color_res = pick_color(result)
                win = 0
                
                if bet_type == '🔢 Number':
                    if result == number:
                        win = bet * 35
                else:
                    if color_res == color:
                        win = bet * 2

                st.session_state.balance += (win - bet)
                
                # Display result with color coding
                result_color = '🔴' if color_res == 'red' else ('⚫' if color_res == 'black' else '🟢')
                st.markdown(f'<div style="text-align:center; font-size:60px; font-weight:bold; padding:20px; background:#f0f0f0; border-radius:10px;">{result_color} {result}</div>', unsafe_allow_html=True)
                
                if win > 0:
                    st.success(f'🎉 **WIN!** Result: {result} ({color_res}) — Won: **${win:.2f}** — New Balance: **${st.session_state.balance:.2f}**')
                else:
                    st.info(f'😞 Result: {result} ({color_res}) — Lost ${bet:.2f} — New Balance: ${st.session_state.balance:.2f}')

    st.divider()
    st.write('Balance:', st.session_state.get('balance', 0))
