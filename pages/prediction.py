import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

st.title("📈 스트레스 지수 예측")
st.caption("오늘의 기분과 수면 패턴을 반영한 AI 예측 모델")

# ---------------------------------------------------
# app.py에서 선택한 기분 불러오기
# ---------------------------------------------------
mood_score_map = {
    "😊 행복": +7,
    "🙂 보통": +3,
    "😥 스트레스": -3,
    "😭 매우 스트레스": -7
}

if "selected_mood" in st.session_state:
    selected_mood = st.session_state["selected_mood"]
    mood_effect = mood_score_map[selected_mood]
else:
    selected_mood = "🙂 보통"
    mood_effect = 0

st.info(f"오늘 선택한 기분: **{selected_mood}** → 예측 영향값: `{mood_effect}`")

# ---------------------------------------------------
# 가상 60일 데이터 생성
# ---------------------------------------------------
today = datetime.today()
dates = [today - timedelta(days=i) for i in range(60)]
dates = sorted(dates)

rng = np.random.default_rng(42)
stress_vals = np.clip(rng.normal(70, 10, 60), 20, 100)
sleep_vals = np.clip(rng.normal(7, 1.2, 60), 4, 10)

df = pd.DataFrame({
    "날짜": dates,
    "스트레스": stress_vals,
    "수면": sleep_vals
})

# ---------------------------------------------------
# AI 예측 함수 (EMA + 수면 + 기분 영향)
# ---------------------------------------------------
def ai_predict(stress_series, sleep_today, mood_effect):
    ema_pred = stress_series.ewm(span=5).mean().iloc[-1]

    sleep_effect = 0
    if sleep_today < 5:
        sleep_effect += 10
    elif sleep_today < 6:
        sleep_effect += 5

    final_pred = ema_pred + sleep_effect + mood_effect
    return float(np.clip(final_pred, 0, 100))

# 오늘 상태
today_stress = df.iloc[-1]["스트레스"]
today_sleep = df.iloc[-1]["수면"]

predicted_tomorrow = ai_predict(df["스트레스"], today_sleep, mood_effect)

# ---------------------------------------------------
# 내일 예측 결과
# ---------------------------------------------------
st.subheader("🎯 내일의 스트레스 지수")
st.metric("예측 결과", f"{predicted_tomorrow:.1f} 점")

# ---------------------------------------------------
# 1주일 예측
# ---------------------------------------------------
future_preds = []
fake_series = df["스트레스"].copy()
current_sleep = today_sleep

for _ in range(7):
    next_pred = ai_predict(fake_series, current_sleep, mood_effect)
    future_preds.append(next_pred)
    fake_series = pd.concat([fake_series, pd.Series([next_pred])], ignore_index=True)

future_dates = [today + timedelta(days=i+1) for i in range(7)]

df_future = pd.DataFrame({
    "날짜": future_dates,
    "예측 스트레스": future_preds
})

st.subheader("📈 향후 7일 스트레스 예측")
st.line_chart(df_future.set_index("날짜"))

# ---------------------------------------------------
# 60일 추세
# ---------------------------------------------------
st.subheader("📘 최근 60일 스트레스 변화")
st.line_chart(df.set_index("날짜")["스트레스"])
