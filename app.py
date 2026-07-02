st.title("📊 FUTURE MATRIX TRADING DASHBOARD")

col1, col2, col3 = st.columns(3)

col1.metric("Weekly Trend", "Bullish")
col2.metric("H4 Structure", "Bullish")
col3.metric("Confidence", "85%")

st.divider()

st.subheader("📍 Trade Decision Screen")

st.success("BUY SIGNAL ACTIVE 🚀")
st.write("Direction: Bullish")
st.write("Risk: Controlled")
st.write("Grade: A+ SETUP")
import streamlit as st
import random
import os
import pandas as pd

# =========================
# LOG FILE
# =========================
log_file = "trade_log.csv"

if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("decision,score,grade,direction,result\n")


# =========================
# ENGINE
# =========================
def generate_signal():
    weekly = random.choice(["bullish", "bearish"])
    h4 = random.choice(["bullish", "bearish"])
    m15 = random.choice(["yes", "no"])
    liquidity = random.choice(["yes", "no"])
    risk = "yes"

    score = 0
    direction = None

    if weekly == h4:
        score += 50
        direction = weekly
    else:
        score += 10

    if m15 == "yes":
        score += 20

    if liquidity == "yes":
        score += 20
    else:
        score -= 10

    if risk == "yes":
        score += 10

    if score >= 85:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 60:
        grade = "B"
    else:
        grade = "NO TRADE"

    return score, direction, grade


def simulate_result():
    return random.choice(["win", "loss", "skip"])


# =========================
# APP UI
# =========================
st.set_page_config(page_title="Future Matrix", layout="centered")

st.title("📊 FUTURE MATRIX PROP FIRM")
st.subheader("Trading Dashboard System")

# =========================
# BUTTONS
# =========================
col1, col2 = st.columns(2)

with col1:
    run = st.button("🚀 RUN TRADE")

with col2:
    auto = st.button("🤖 AUTO TRADE")


# =========================
# SESSION STATE
# =========================
if "balance" not in st.session_state:
    st.session_state.balance = 1000

# =========================
# RUN TRADE
# =========================
if run or auto:

    score, direction, grade = generate_signal()
    result = simulate_result()

    # update balance
    if result == "win":
        st.session_state.balance += 10
    elif result == "loss":
        st.session_state.balance -= 10

    # save log
    with open(log_file, "a") as f:
        f.write(f"BUY,{score},{grade},{direction},{result}\n")

    st.success("Trade Executed!")

    st.metric("Score", score)
    st.metric("Grade", grade)
    st.metric("Result", result)
    st.metric("Balance", st.session_state.balance)


# =========================
# DASHBOARD
# =========================
st.divider()
st.subheader("📈 Performance Dashboard")

data = pd.read_csv(log_file)

wins = len(data[data["result"] == "win"])
losses = len(data[data["result"] == "loss"])
total = len(data)

winrate = (wins / total * 100) if total > 0 else 0

st.write(f"Trades: {total}")
st.write(f"Wins: {wins}")
st.write(f"Losses: {losses}")
st.write(f"Win Rate: {round(winrate, 2)}%")


# =========================
# EQUITY CURVE
# =========================
st.subheader("📉 Equity Curve")

balance = 1000
equity = []

for r in data["result"]:
    if r == "win":
        balance += 10
    elif r == "loss":
        balance -= 10
    equity.append(balance)

st.line_chart(equity)
