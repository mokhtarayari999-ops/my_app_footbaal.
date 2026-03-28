import streamlit as st
import pandas as pd
import random
from collections import Counter

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="المحلل التونسي - برو 2026", page_icon="🏆", layout="centered")

# 2. تصميم CSS احترافي (ألوان الرابطة المحترفة)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background: linear-gradient(45deg, #1e3c72, #2a5298); color: white; font-weight: bold; border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .stButton>button:hover { background: linear-gradient(45deg, #2a5298, #1e3c72); transform: scale(1.02); transition: 0.3s; }
    .stat-box { background-color: #f1f3f5; padding: 15px; border-radius: 12px; text-align: center; border-bottom: 4px solid #1e3c72; }
    .standings-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 0.9em; }
    .standings-table th { background-color: #1e3c72; color: white; padding: 10px; }
    .standings-table td { padding: 8px; border-bottom: 1px solid #ddd; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهوية البصرية
st.markdown("<h1 style='text-align: center; color: #1e3c72;'>🇹🇳 المحلل التونسي المحترف</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>نظام المحاكاة الذكي - الرابطة المحترفة الأولى 2026</p>", unsafe_allow_html=True)

# 4. قاعدة البيانات الشاملة (الفرق + الترتيب)
data = [
    {'n': 'الترجي التونسي (EST)', 'pts': 42, 'w': 13, 'sc': 1.85, 'con': 0.25, 'crn': 6.2},
    {'n': 'النادي الإفريقي (CA)', 'pts': 38, 'w': 11, 'sc': 1.55, 'con': 0.35, 'crn': 5.8},
    {'n': 'الاتحاد المنستيري (USM)', 'pts': 35, 'w': 10, 'sc': 1.25, 'con': 0.55, 'crn': 4.8},
    {'n': 'النادي الصفاقسي (CSS)', 'pts': 31, 'w': 8, 'sc': 1.40, 'con': 0.45, 'crn': 5.2},
    {'n': 'الملعب التونسي (ST)', 'pts': 28, 'w': 7, 'sc': 1.15, 'con': 0.42, 'crn': 5.0},
    {'n': 'النجم الساحلي (ESS)', 'pts': 24, 'w': 6, 'sc': 1.10, 'con': 0.75, 'crn': 4.5}
]
df = pd.DataFrame(data)

# 5. منطقة اختيار الفرق وإحصائيات فورية
st.markdown("### 🏟️ إعداد المباراة")
col1, col2 = st.columns(2)
with col1:
    h_name = st.selectbox("🏠 مستضيف الأرض", df['n'], index=0)
    h_data = df[df['n'] == h_name].iloc[0]
    st.markdown(f"<div class='stat-box'>🔥 الهجوم: {h_data['sc']}<br>🛡️ الدفاع: {h_data['con']}</div>", unsafe_allow_html=True)

with col2:
    a_name = st.selectbox("✈️ الفريق الضيف", df['n'], index=1)
    a_data = df[df['n'] == a_name].iloc[0]
    st.markdown(f"<div class='stat-box'>🔥 الهجوم: {a_data['sc']}<br>🛡️ الدفاع: {a_data['con']}</div>", unsafe_allow_html=True)

# 6. محرك التوقعات
st.write("")
if st.button("📊 تشغيل المحلل الرقمي"):
    with st.status("جاري معالجة البيانات...", expanded=True) as status:
        st.write("تحليل القوة الهجومية...")
        st.write("مقارنة الصلابة الدفاعية...")
        trials = 5000
        res, hw, d, aw = [], 0, 0, 0
        for _ in range(trials):
            hg = round((h_data['sc'] * (a_data['con']/1.1)) * random.uniform(0.6, 1.4))
            ag = round((a_data['sc'] * (h_data['con']/1.1)) * random.uniform(0.6, 1.4))
            res.append(f"{hg}-{ag}")
            if hg > ag: hw += 1
            elif ag > hg: aw += 1
            else: d += 1
        status.update(label="اكتمل التحليل!", state="complete", expanded=False)

    # عرض النتائج بأسلوب البطاقات
    st.balloons()
    st.markdown("### 🎯 توقعات المباراة")
    c1, c2, c3 = st.columns(3)
    c1.metric("فوز الأرض", f"{(hw/50):.1f}%", "🏠")
    c2.metric("تعادل", f"{(d/50):.1f}%", "🤝")
    c3.metric("فوز الضيف", f"{(aw/50):.1f}%", "✈️")
    
    st.success(f"📌 النتيجة الأكثر تكراراً في المحاكاة: **{Counter(res).most_common(1)[0][0]}**")

# 7. جدول الترتيب في الأسفل
st.markdown("---")
st.markdown("### 📈 جدول ترتيب الدوري (2026)")
st.table(df[['n', 'pts', 'w']].rename(columns={'n': 'الفريق', 'pts': 'النقاط', 'w': 'الفوز'}))

st.caption("حقوق الطبع محفوظة © 2026 | شريكك الذكي")

