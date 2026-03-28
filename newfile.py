import streamlit as st
import pandas as pd
import random
from collections import Counter

# 1. إعدادات الصفحة المتقدمة (أيقونة وتنسيق)
st.set_page_config(page_title="المحلل التونسي البريميوم", page_icon="🇹🇳", layout="centered")

# 2. لمسة جمالية بالـ CSS لتغيير الألوان والخلفيات
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3.5em; background-image: linear-gradient(to right, #ed213a, #93291e); color: white; font-weight: bold; border: none; }
    .result-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 10px; border-right: 5px solid #ed213a; }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #93291e;'>🏆 المحلل الرياضي الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>الرابطة المحترفة الأولى - نسخة 2026 المحدثة</p>", unsafe_allow_html=True)

# 4. قاعدة البيانات الموسعة (معدلات محدثة)
tunisia_db = [
    {'n': 'الترجي التونسي (EST)', 'sc': 1.85, 'con': 0.25, 'crn': 6.2, 'crd': 1.8},
    {'n': 'النادي الإفريقي (CA)', 'sc': 1.55, 'con': 0.35, 'crn': 5.8, 'crd': 2.1},
    {'n': 'النجم الساحلي (ESS)', 'sc': 1.10, 'con': 0.75, 'crn': 4.5, 'crd': 2.5},
    {'n': 'النادي الصفاقسي (CSS)', 'sc': 1.40, 'con': 0.45, 'crn': 5.2, 'crd': 1.9},
    {'n': 'الاتحاد المنستيري (USM)', 'sc': 1.25, 'con': 0.55, 'crn': 4.8, 'crd': 2.3},
    {'n': 'الملعب التونسي (ST)', 'sc': 1.15, 'con': 0.42, 'crn': 5.0, 'crd': 2.0}
]

df = pd.DataFrame(tunisia_db)

# 5. واجهة الاختيار بشكل منسق
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        h_name = st.selectbox("🏠 فريق الأرض", df['n'], index=0)
    with col2:
        a_name = st.selectbox("✈️ فريق الضيف", df['n'], index=1)

h = df[df['n'] == h_name].iloc[0]
a = df[df['n'] == a_name].iloc[0]

# 6. زر التحليل مع أنيميشن
if st.button("🔥 تحليل المباراة وتوليد التوقعات"):
    with st.spinner('جاري إجراء 5000 محاكاة رقمية...'):
        trials = 5000
        res, hw, d, aw, o25 = [], 0, 0, 0, 0
        
        for _ in range(trials):
            hg = round((h['sc'] * (a['con']/1.1)) * random.uniform(0.6, 1.4))
            ag = round((a['sc'] * (h['con']/1.1)) * random.uniform(0.6, 1.4))
            res.append(f"{hg}-{ag}")
            if hg > ag: hw += 1
            elif ag > hg: aw += 1
            else: d += 1
            if (hg + ag) > 2.5: o25 += 1
            
        # حساب الركنيات والبطاقات بشكل عشوائي مدروس
        total_corners = round((h['crn'] + a['crn']) * random.uniform(0.8, 1.2), 1)
        total_cards = round((h['crd'] + a['crd']) * random.uniform(0.7, 1.3), 1)

    # 7. عرض النتائج بشكل "بريميوم"
    st.markdown("---")
    
    # بطاقة النتيجة المتوقعة
    st.markdown(f"""
    <div class="result-card">
        <h3 style='margin:0;'>🎯 النتيجة الأكثر احتمالية: <span style='color:#ed213a;'>{Counter(res).most_common(1)[0][0]}</span></h3>
        <p style='margin:5px 0 0 0; color:gray;'>بناءً على تفوق الهجوم والدفاع التاريخي</p>
    </div>
    """, unsafe_allow_html=True)

    # إحصائيات المباراة
    c1, c2, c3 = st.columns(3)
    c1.metric("فوز {0}".format(h_name.split()[0]), f"{(hw/50):.1f}%")
    c2.metric("التعادل", f"{(d/50):.1f}%")
    c3.metric("فوز {0}".format(a_name.split()[0]), f"{(aw/50):.1f}%")

    # إحصائيات إضافية
    st.info(f"🚩 **الركنيات المتوقعة:** {total_corners} | 🟨 **البطاقات المتوقعة:** {total_cards}")
    
    if (o25/50) > 50:
        st.warning(f"⚠️ تنبيه: احتمال عالي لأكثر من 2.5 أهداف بنسبة {(o25/50):.1f}%")

st.markdown("<p style='text-align: center; font-size: 0.8em; color: gray;'>تحذير: هذه التوقعات مبنية على محاكاة إحصائية ولا تضمن النتائج الحقيقية.</p>", unsafe_allow_html=True)
    
