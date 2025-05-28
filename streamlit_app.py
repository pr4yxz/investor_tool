import streamlit as st
from checklist import evaluate

st.set_page_config(page_title="Investor Checklist", layout="centered")

st.title("📊 Investor Checklist Tool")
st.write("วิเคราะห์หุ้นตามเกณฑ์พื้นฐาน 6 ข้อแบบ Warren Buffett")

ticker = st.text_input("กรอกชื่อหุ้น (เช่น TSLA, UNH, ASML):", value="TSLA")

if st.button("วิเคราะห์"):
    try:
        result = evaluate(ticker.strip().upper())
        st.success("ผลลัพธ์:")
        st.json(result)
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")