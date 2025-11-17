import streamlit as st
import numpy as np
import pandas as pd

# =============================
# 스타일 적용
# =============================
st.markdown("""
<style>
.card {
    background-color: white;
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.07);
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 스트레스 지수 예측")
st.caption("가벼운 AI 모델을 사용하여 내일 / 1주일 뒤 스트레스 지수를 예측합니다.")

# ---------- 예측 함수 ----------
def predict_tomorrow(last_seq):
    return np.mean(last_seq)

def predict_week(last_seq):
    preds = []
    seq = last_seq.copy()
    for _ in range(7):
        tomorrow = np.mean(seq)
        preds.append(tomorrow)
        seq = np.append(seq[1:], tomorrow)
    return preds

# ---------- 입력 ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📥 최근 7일 자율신경활성도 입력")
user_input = st.text_input("예: 50,52,55,53,51,49,50", "")

if st.button("예측하기"):
    try:
        last_seq = np.array(list(map(float, user_input.split(","))))
        if len(last_seq) != 7
