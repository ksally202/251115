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

# ---------------------------------------------------
# 오늘의 기분 선택
# ---------------------------------------------------
st.markdown("## 😊 오늘의 기분을 선택해주세요")
mood = st.segmented_control(
    "오늘 기분",
    ["😊 행복", "🙂 보통", "😥 스트레스", "😭 매우 스트레스"]
)
st.write(f"**오늘의 기분:** {mood}")

st.markdown("---")

# ---------------------------------------------------
# 오늘 스트레스 지수 (데모용)
# ---------------------------------------------------
today_stress = np.random.randint(25, 90)

st.markdown("## 📊 오늘의 스트레스 지수")
st.metric("스트레스 지수", f"{today_stress} / 100")

with st.expander("🔮 더보기 (내일/1주일 예측은 2번째 페이지에서 확인하세요!)"):
    st.write("예측 기능은 왼쪽 메뉴의 **📈 스트레스 지수 예측** 페이지에서 확인할 수 있어요.")

st.markdown("---")

# ---------------------------------------------------
# 추천
# ---------------------------------------------------
st.markdown("## 🍵 오늘의 추천")
st.info("카페인을 오늘 많이 섭취했다면, 따뜻한 허브티와 가벼운 산책을 추천드려요 😊")

st.video("https://www.youtube.com/watch?v=UBMk30rjy0o")

st.markdown("---")

# ---------------------------------------------------
# 프리미엄 기능
# ---------------------------------------------------
st.markdown("## 🔒 프리미엄 기능: 수면 패턴 분석")
premium = st.checkbox("🔓 프리미엄 잠금 해제")

if not premium:
    st.warning("이 기능은 프리미엄 이용자에게만 제공됩니다.")
else:
    sleep_hours = np.random.randint(4, 9, size=7)
    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Sleep": sleep_hours
    })
    st.write("### 💤 1주일 수면 패턴(꺾은선 그래프)")
    st.line_chart(df, x="Day", y="Sleep")

st.markdown("---")

# ---------------------------------------------------
# Q&A: 수면시간 측정 방법
# ---------------------------------------------------
with st.container():
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    st.subheader("❓ 수면 시간은 어떻게 측정하나요?")

    with st.expander("답변 보기"):
        st.markdown("""
**Q. 수면시간은 어떻게 계산되나요?**  
A. 실제 서비스에서는 스마트폰·스마트워치의 **움직임 센서, 심박수, 화면 사용 패턴**을 기반으로  
잠든 시점과 깨어난 시점을 추정합니다.

**Q. 완벽하게 정확한가요?**  
A. 100% 정확하지는 않습니다.  
예를 들어 독서 중 화면이 꺼져 있을 때처럼, 실제로는 안 잤지만 기기가 수면으로 판단할 수도 있습니다.

**Q. 더 정확한 방법은 있나요?**  
A. 네. 웨어러블(스마트워치)을 함께 사용하면  
심박수·움직임 데이터를 함께 분석하므로  
**얕은 잠/깊은 잠까지 측정할 수 있어 훨씬 정확**해집니다.
""")

st.caption("© 2025 ALL DAY Stress Out")

