import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="المحلل التونسي المحترف", layout="centered")

# 2. إضافة التنسيقات (CSS) لمطابقة واجهة الصورة بدقة
st.markdown("""
    <style>
    /* تنسيق الحاوية الرئيسية والخطوط */
    .main { direction: rtl; text-align: right; background-color: #fcfcfc; }
    h1, h2, h3, p { text-align: center; font-family: 'Arial'; color: #333; }
    
    /* تنسيق مربعات الإحصائيات (الهجوم والدفاع) */
    .stat-card {
        background-color: white;
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        text-align: right;
    }
    .stat-title { color: #888; font-size: 14px; margin-bottom: 5px; }
    .stat-value { color: #333; font-size: 26px; font-weight: bold; }
    
    /* تنسيق زر التحديث */
    .stButton>button {
        width: 100%;
        background-color: white;
        color: #555;
        border: 1px solid #ddd;
        border-radius: 5px;
        height: 3em;
    }
    
    /* تحسين عرض الجداول */
    .stDataFrame { margin: 0 auto; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي كما في الصورة
st.markdown("<h1>المحلل التونسي المحترف 🇹🇳</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray; font-size:14px;'>نظام المحاكاة الذكي - الرابطة المحترفة الأولى</p>", unsafe_allow_html=True)

st.write("") 

# 4. قسم إعداد المباراة
st.markdown("<h3>⚽ إعداد المباراة</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# عمود الفريق المستضيف
with col1:
    st.markdown("<p style='text-align:right; font-size:13px;'>🏠 الفريق المستضيف</p>", unsafe_allow_html=True)
    st.selectbox("", ["الترجي الرياضي", "النجم الساحلي", "النادي الصفاقسي"], key="home", label_visibility="collapsed")
    
    # مربع الهجوم
    st.markdown('<div class="stat-card"><div class="stat-title">🔥 قوة الهجوم</div><div class="stat-value">1.85</div></div>', unsafe_allow_html=True)
    # مربع الدفاع
    st.markdown('<div class="stat-card"><div class="stat-title">🛡️ قوة الدفاع</div><div class="stat-value">0.20</div></div>', unsafe_allow_html=True)

# عمود الفريق الضيف
with col2:
    st.markdown("<p style='text-align:right; font-size:13px;'>✈️ الفريق الضيف</p>", unsafe_allow_html=True)
    st.selectbox("", ["النادي الإفريقي", "الاتحاد المنستيري", "الملعب التونسي"], key="away", label_visibility="collapsed")
    
    # مربع الهجوم
    st.markdown('<div class="stat-card"><div class="stat-title">🔥 قوة الهجوم</div><div class="stat-value">1.55</div></div>', unsafe_allow_html=True)
    # مربع الدفاع
    st.markdown('<div class="stat-card"><div class="stat-title">🛡️ قوة الدفاع</div><div class="stat-value">0.35</div></div>', unsafe_allow_html=True)

st.write("")

# 5. جدول الترتيب الحالي (البيانات مطابقة للصورة)
st.markdown("<h3>📊 جدول الترتيب الحالي</h3>", unsafe_allow_html=True)

data = {
    'الفريق': ['الترجي الرياضي', 'النادي الإفريقي', 'الاتحاد المنستيري', 'الملعب التونسي', 'النجم الساحلي', 'النادي الصفاقسي'],
    'لعب': [14, 14, 14, 14, 14, 14],
    'فوز': [12, 11, 10, 8, 7, 6],
    'نقاط': [42, 38, 35, 31, 28, 24]
}
df = pd.DataFrame(data)

# عرض الجدول بشكل كامل وواضح
st.dataframe(df, use_container_width=True, hide_index=True)

# 6. زر التحديث والذيل
if st.button('🔄 تحديث البيانات الآن'):
    st.rerun()

st.markdown("<br><p style='font-size: 12px; color: gray;'>جميع الحقوق محفوظة © المحلل التونسي 2026</p>", unsafe_allow_html=True)
    
