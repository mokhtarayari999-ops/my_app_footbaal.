import streamlit as st
import random

# 1. إعدادات الصفحة والتصميم (CSS) للتطابق مع الصورة
st.set_page_config(page_title="المحلل الرياضي الذكي", page_icon="🏆", layout="centered")

st.markdown("""
    <style>
    .main { direction: rtl; text-align: center; font-family: 'Arial'; }
    .main-title { color: #8B1A1A; font-size: clamp(30px, 8vw, 45px); font-weight: bold; margin-bottom: 0px; }
    .sub-title { color: #555; font-size: 16px; margin-bottom: 20px; }
    label { font-size: 18px !important; font-weight: bold !important; text-align: right !important; display: block !important; margin-bottom: 5px; }
    
    /* تنسيق الزر الأحمر */
    div.stButton > button {
        background-color: #E31E24 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 12px 25px !important;
        font-size: 18px !important;
        width: 100% !important;
        border: none !important;
        transition: 0.3s;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #8B1A1A;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة بيانات الفرق (قوة الهجوم والدفاع الافتراضية)
teams_data = {
    "(EST) الترجي التونسي": {"atk": 2.5, "def": 0.8},
    "(CA) النادي الإفريقي": {"atk": 1.8, "def": 1.1},
    "(ESS) النجم الساحلي": {"atk": 1.9, "def": 1.0},
    "(CSS) النادي الصفاقسي": {"atk": 1.6, "def": 0.9},
    "(USM) الاتحاد المنستيري": {"atk": 2.0, "def": 1.2},
    "(ST) الملعب التونسي": {"atk": 1.7, "def": 1.3}
}

# 3. واجهة التطبيق
st.markdown('<div style="font-size:50px; text-align:center;">🏆</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">المحلل الرياضي<br>الذكي</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">الرابطة المحترفة الأولى - نسخة 2026 المحدثة</p>', unsafe_allow_html=True)

# اختيارات الفرق
home_team = st.selectbox("🏠 فريق الأرض", list(teams_data.keys()), index=0)
away_team = st.selectbox("✈️ فريق الضيف", list(teams_data.keys()), index=1)

# 4. النظام الحسابي للتحليل
def predict_score(home, away):
    # حساب الأهداف بناءً على الهجوم ضد الدفاع + عامل الأرض (0.2)
    home_expected = (teams_data[home]["atk"] - teams_data[away]["def"]) + 1.2 + random.uniform(-0.5, 0.5)
    away_expected = (teams_data[away]["atk"] - teams_data[home]["def"]) + 0.8 + random.uniform(-0.5, 0.5)
    
    return max(0, int(round(home_expected))), max(0, int(round(away_expected)))

# الزر والنتيجة
if st.button("🔥 تحليل المباراة وتوليد التوقعات"):
    if home_team == away_team:
        st.warning("الرجاء اختيار فريقين مختلفين!")
    else:
        with st.spinner('جاري معالجة البيانات الإحصائية...'):
            h_score, a_score = predict_score(home_team, away_team)
            
            st.markdown(f"""
                <div class="result-box">
                    <h3>النتيجة المتوقعة ⚽</h3>
                    <h2 style="color:#8B1A1A;">{h_score} : {a_score}</h2>
                    <p><b>{home_team}</b> ضد <b>{away_team}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            # نصيحة المحلل
            if h_score > a_score: st.info(f"💡 المحلل ينصح بـ: فوز {home_team}")
            elif a_score > h_score: st.info(f"💡 المحلل ينصح بـ: فوز {away_team}")
            else: st.info("💡 المحلل ينصح بـ: تعادل إيجابي")

st.markdown("<p style='color:gray; font-size:12px; margin-top:30px;'>تحذير: هذه التوقعات مبنية على محاكاة إحصائية ولا تضمن النتائج الحقيقية.</p>", unsafe_allow_html=True)
