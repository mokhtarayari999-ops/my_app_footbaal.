import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة لتناسب الجوال والمتصفحات
st.set_page_config(
    page_title="المحلل التونسي المحترف",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تحسين المظهر (CSS) ليكون متناسقاً مع واجهة الهاتف
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #f8f9fa; }
    .main { text-align: right; direction: rtl; }
    h1, h2, h3 { color: #003366; text-align: center; font-family: 'Arial'; }
    .stSelectbox label { text-align: right; font-weight: bold; width: 100%; }
    div[data-testid="stMetric"] { background-color: white; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("المحلل التونسي المحترف 🇹🇳")
st.markdown("<p style='text-align: center; color: gray;'>نظام المحاكاة الذكي - الرابطة المحترفة الأولى</p>", unsafe_allow_html=True)

st.divider()

# 3. قسم اختيار الفرق (سيتوزع تلقائياً على الهاتف)
st.subheader("إعداد المباراة ⚽")
col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox("الفريق المستضيف 🏠", ["الترجي الرياضي", "الاتحاد المنستيري", "النادي الصفاقسي", "النجم الساحلي"], index=0)
    st.metric(label="قوة الهجوم 🔥", value="1.85")
    st.metric(label="قوة الدفاع 🛡️", value="0.20")

with col2:
    away_team = st.selectbox("الفريق الضيف ✈️", ["النادي الإفريقي", "الملعب التونسي", "اتحاد بن قردان", "قوافل قفصة"], index=0)
    st.metric(label="قوة الهجوم 🔥", value="1.55")
    st.metric(label="قوة الدفاع 🛡️", value="0.35")

st.divider()

# 4. جدول الترتيب (تنسيق تلقائي للعرض)
st.subheader("جدول الترتيب الحالي 📊")

data = {
    'الفريق': ['الترجي الرياضي', 'النادي الإفريقي', 'الاتحاد المنستيري', 'الملعب التونسي', 'النجم الساحلي', 'النادي الصفاقسي'],
    'لعب': [14, 14, 14, 14, 14, 14],
    'الفوز': [13, 11, 10, 8, 7, 6],
    'النقاط': [42, 38, 35, 31, 28, 24]
}

df = pd.DataFrame(data)

# عرض الجدول ليأخذ كامل عرض شاشة الهاتف
st.dataframe(
    df.style.set_properties(**{'text-align': 'center'}),
    use_container_width=True,
    hide_index=True
)

# 5. زر التحديث
if st.button('تحديث البيانات الآن 🔄', use_container_width=True):
    st.toast("جاري تحديث البيانات من السيرفر...")
    st.rerun()

st.markdown("<br><p style='text-align: center; font-size: 0.8rem;'>جميع الحقوق محفوظة © المحلل التونسي 2026</p>", unsafe_allow_html=True)


