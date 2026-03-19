import streamlit as st

st.set_page_config(page_title="NEURONEST OS", layout="wide")

st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
        font-family: 'Inter', sans-serif;
    }

    h1 {
        border-bottom: 3px solid #2563EB;
        padding-bottom: 8px;
    }

    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }

    div.stButton > button {
        background-color: #FFFFFF;
        color: #2563EB;
        border: 1px solid #CBD5F5;
        border-radius: 10px;
        padding: 12px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #EFF6FF;
        border-color: #2563EB;
    }

    .primary-btn button {
        background-color: #2563EB !important;
        color: white !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

def go(page):
    st.session_state.page = page

menu = [
    "Home",
    "Behavior Prediction",
    "Biological Data",
    "Resource Management",
    "Temporal Memory"
]

st.sidebar.markdown("## NEURONEST")
st.sidebar.caption("Smart Home Control")

choice = st.sidebar.radio("Menu", menu, index=menu.index(st.session_state.page))

if choice != st.session_state.page:
    st.session_state.page = choice
    st.rerun()

if st.session_state.page == "Home":

    st.markdown("<h1>ภาพรวมระบบ</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("เครือข่าย", "ออนไลน์", "เสถียร")
    col2.metric("อุณหภูมิ", "24.5°C", "-0.2")
    col3.metric("พลังงาน", "98%", "กำลังชาร์จ")

    st.markdown("### เลือกระบบที่ต้องการใช้งาน")

    colA, colB = st.columns(2)

    if colA.button("Behavior Prediction", use_container_width=True):
        go("Behavior Prediction")
        st.rerun()

    if colB.button("Biological Data", use_container_width=True):
        go("Biological Data")
        st.rerun()

    colC, colD = st.columns(2)

    if colC.button("Resource Management", use_container_width=True):
        go("Resource Management")
        st.rerun()

    if colD.button("Temporal Memory", use_container_width=True):
        go("Temporal Memory")
        st.rerun()

else:
    st.markdown(f"<h1>{st.session_state.page}</h1>", unsafe_allow_html=True)

    if st.button("กลับหน้าหลัก"):
        go("Home")
        st.rerun()

    st.markdown("---")

    if st.session_state.page == "Behavior Prediction":

        st.info("กรอกสถานะของคุณ ระบบจะปรับบ้านให้เหมาะสมโดยอัตโนมัติ")

        col1, col2 = st.columns(2)

        with col1:
            state = st.selectbox("ตอนนี้คุณกำลัง...", ["ตื่นนอน", "ทำงาน", "พักผ่อน"])

        with col2:
            time = st.selectbox("ช่วงเวลา", ["เช้า", "กลางวัน", "เย็น", "กลางคืน"])

        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        if st.button("ให้ระบบจัดการอัตโนมัติ", use_container_width=True):

            result = []

            if state == "ตื่นนอน":
                result += ["เปิดม่านรับแสงธรรมชาติ", "เปิดเพลงเบา ๆ"]

            elif state == "ทำงาน":
                result += ["เพิ่มความสว่างของไฟ", "ปิดเสียงรบกวน"]

            elif state == "พักผ่อน":
                result += ["ลดแสงไฟ", "เปิดโหมดผ่อนคลาย"]

            if time == "กลางคืน":
                result.append("เปิดโหมดแสงอุ่น")

            st.success("ระบบกำลังดำเนินการ")
            for r in result:
                st.write("•", r)
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.page == "Biological Data":

        st.info("กรอกข้อมูลร่างกาย ระบบจะปรับสภาพแวดล้อมให้เหมาะกับคุณ")

        stress = st.slider("ระดับความเครียด", 0, 100, 30)
        energy = st.slider("พลังงานร่างกาย", 0, 100, 60)

        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        if st.button("วิเคราะห์และปรับ", use_container_width=True):

            result = []

            if stress > 70:
                result += ["ลดแสงไฟ", "เปิดเสียงธรรมชาติ"]
            else:
                result.append("สภาพแวดล้อมปกติ")

            if energy < 40:
                result.append("เพิ่มแสงเพื่อกระตุ้นความตื่นตัว")

            st.success("ปรับสภาพเรียบร้อย")
            for r in result:
                st.write("•", r)
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.page == "Resource Management":

        st.info("ตรวจสอบทรัพยากรในบ้าน และให้ระบบช่วยจัดการอัตโนมัติ")

        water = st.slider("ระดับน้ำคงเหลือ", 0, 100, 80)
        food = st.slider("อาหารคงเหลือ", 0, 100, 60)

        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        if st.button("วิเคราะห์ทรัพยากร", use_container_width=True):

            result = []

            if water < 30:
                result.append("ควรสั่งซื้อน้ำเพิ่ม")

            if food < 30:
                result.append("ควรสั่งอาหารเพิ่ม")

            if not result:
                result.append("ทรัพยากรเพียงพอ")

            st.success("วิเคราะห์เสร็จแล้ว")
            for r in result:
                st.write("•", r)
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.page == "Temporal Memory":

        st.info("เลือกวันที่ ระบบจะจำลองสภาพแวดล้อมในวันนั้น")

        date = st.date_input("เลือกวันที่")

        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        if st.button("โหลดข้อมูล", use_container_width=True):

            st.success("โหลดข้อมูลสำเร็จ")
            st.write("• อุณหภูมิ: 25°C")
            st.write("• แสง: ปกติ")
            st.write("• โหมด: พักผ่อน")
        st.markdown('</div>', unsafe_allow_html=True)
