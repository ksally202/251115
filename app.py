import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="ALL DAY Stress Out",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 ALL DAY Stress Out")
st.write("AI 기반 감정·스트레스·수면을 한 번에 관리하는 서비스입니다.")

st.markdown("## 😊 오늘의 기분을 선택해주세요")
mood = st.segmented_control(
    "오늘 기분",
    ["😊 행복", "🙂 보통", "😥 스트레스", "😭 매우 스트레스"]
)
st.write(f"**오늘의 기분:** {mood}")

st.markdown("---")

# 오늘 스트레스 지수 (데모용)
today_stress = np.random.randint(25, 90)

st.markdown("## 📊 오늘의 스트레스 지수")
st.metric("스트레스 지수", f"{today_stress} / 100")

with st.expander("🔮 더보기 (내일/1주일 예측은 2번째 페이지에서 확인하세요!)"):
    st.write("예측 기능은 왼쪽 메뉴의 **📈 스트레스 지수 예측** 페이지에서 확인할 수 있어요.")

st.markdown("---")

st.markdown("## 🍵 오늘의 추천")
st.info("카페인을 오늘 많이 섭취했다면, 따뜻한 허브티와 가벼운 산책을 추천드려요 😊")

st.video("https://www.youtube.com/watch?v=UBMk30rjy0o")

st.markdown("---")

st.markdown("## 🔒 프리미엄 기능: 수면 패턴 분석")
premium = st.checkbox("🔓 프리미엄 잠금 해제")

if not premium:
    st.warning("이 기능은 프리미엄 이용자에게만 제공됩니다.")
else:
    sleep_hours = np.random.randint(4, 9, size=7)
    df = pd.DataFrame({"Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "Sleep": sleep_hours})
    st.bar_chart(df, x="Day", y="Sleep")

st.markdown("---")
st.caption("© 2025 ALL DAY Stress Out")
