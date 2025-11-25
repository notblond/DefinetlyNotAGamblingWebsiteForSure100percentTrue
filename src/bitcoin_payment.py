"""
Bitcoin payment verification module for NotGamble.
Checks if a payment of 0.0001 BTC has been received to the wallet.
Uses Blockchain.com API (free, no auth required).

Educational use only.
"""

import requests
import time

WALLET_ADDRESS = "bc1p0dakve9q7n726g5qf94gfzzs4t7a7z0qw3unwdyh509n8ujc5m5sk7tg75"
REQUIRED_PAYMENT = 0.0001  # BTC
SATOSHI_PER_BTC = 100_000_000

def get_wallet_balance(address):
    """
    Fetch wallet balance from Blockchain.com API.
    Returns balance in BTC, or None if error.
    """
    try:
        url = f"https://blockchain.info/q/addressbalance/{address}"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            satoshis = int(resp.text)
            btc = satoshis / SATOSHI_PER_BTC
            return btc
    except Exception as e:
        print(f"Error fetching wallet balance: {e}")
    return None


def check_payment_received(min_amount=REQUIRED_PAYMENT):
    """
    Check if payment >= min_amount BTC has been received.
    Returns True if payment received, False otherwise.
    """
    balance = get_wallet_balance(WALLET_ADDRESS)
    if balance is not None:
        return balance >= min_amount
    return False


def get_wallet_info():
    """
    Get wallet address and required payment for display.
    Returns dict with address and required BTC amount.
    """
    return {
        "address": WALLET_ADDRESS,
        "required_btc": REQUIRED_PAYMENT,
        "required_satoshis": int(REQUIRED_PAYMENT * SATOSHI_PER_BTC),
    }
