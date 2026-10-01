import streamlit as st
import os

# إعداد الصفحة
st.set_page_config(
    page_title="أداة كتابة محتوى SEO بالعربية",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم مخصص لدعم العربية
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    * { font-family: 'Cairo', sans-serif; }
    .stApp { direction: rtl; text-align: right; }
    .sidebar .sidebar-content { direction: rtl; text-align: right; }
    h1, h2, h3 { font-family: 'Cairo', sans-serif; }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 700;
        padding: 12px;
    }
    .result-box {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# الحصول على مفتاح API
def get_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        return os.getenv("OPENAI_API_KEY")

api_key = get_api_key()

if not api_key:
    st.error("❌ لم يتم العثور على مفتاح API")
    st.info("💡 إذا كنت تستخدم Streamlit Cloud، أضف المفتاح في Settings > Secrets")
    st.stop()

# استيراد OpenAI بعد التحقق من المفتاح
from openai import OpenAI
client = OpenAI(api_key=api_key)

# العنوان الرئيسي
st.markdown("# ✍️ أداة كتابة محتوى SEO بالعربية")
st.markdown("### اكتب محتوى احترافي متوافق مع محركات البحث باللغة العربية")
