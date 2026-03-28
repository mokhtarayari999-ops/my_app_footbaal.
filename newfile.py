import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="المحلل التونسي 2026", layout="centered")
st.title("⚽ المحلل الرياضي الذكي")
st.subheader("نسخة الرابطة المحترفة الأولى 🇹🇳")

tunisia_db = [
    {'n': 'الترجي التونسي (EST)', 'sc': 1.74, 'con': 0.30},
    {'n': 'النادي الإفريقي (CA)', 'sc': 1.48, 'con': 0.35},
    {'n': 'النجم الساحلي (ESS)', 'sc': 1.00, 'con': 0.82},
    {'n': 'النادي الصفاقسي (CSS)', 'sc': 1.30, 'con': 0.48},
    {'n': 'الملعب التونسي (ST)', 'sc': 1.08, 'con': 0.39},
    {'n': 'الاتحاد المنستيري (USM)', 'sc': 1.00, 'con': 0.60}
]

df = pd.DataFrame(tunisia_db)
h_name = st.selectbox("فريق الأرض", df['n'])
a_name = st.selectbox("فريق الضيف", df['n'])

h = df[df['n'] == h_name].iloc[0]
a = df[df['n'] == a_name].iloc[0]

if st.button("🚀 تحليل المباراة الآن"):
    trials = 3000
    res, hw, d, aw = [], 0, 0, 0
    for _ in range(trials):
        hg = round((h['sc'] * (a['con']/1.1)) * random.uniform(0.5, 1.5))
        ag = round((a['sc'] * (h['con']/1.1)) * random.uniform(0.5, 1.5))
        res.append(f"{hg}-{ag}")
        if hg > ag: hw += 1
        elif ag > hg: aw += 1
        else: d += 1
    
    st.success(f"النتيجة المتوقعة: {Counter(res).most_common(1)[0][0]}")
    st.write(f"🏠 فوز الأرض: {(hw/30):.1f}% | 🤝 تعادل: {(d/30):.1f}% | ✈️ فوز الضيف: {(aw/30):.1f}%")


