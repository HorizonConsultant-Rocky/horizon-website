import streamlit as st
import os

# Page Settings
st.set_page_config(page_title="Horizon Career | Russia Expert", layout="wide")

# Styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .hero-section { background: #1a73e8; color: white; padding: 60px; text-align: center; border-radius: 0 0 30px 30px; }
    .card { background: #f1f3f4; padding: 20px; border-radius: 15px; margin-bottom: 20px; border-top: 5px solid #1a73e8; }
    .footer { background: #202124; color: white; padding: 30px; text-align: center; border-radius: 20px 20px 0 0; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 1. HERO SECTION
st.markdown('<div class="hero-section"><h1>HORIZON CAREER</h1><p>Russia Mein Career Banane Ka Sabse Bharosemand Rasta</p></div>', unsafe_allow_html=True)

if os.path.exists('horizon career.jpeg'):
    st.image('horizon career.jpeg', use_container_width=True)

# 2. INFORMATION SECTION (Bhot Saari Details)
st.header("🇷🇺 Russia: Career Opportunities ka Hub")
c1, c2 = st.columns(2)

with c1:
    st.info("""
    **Education Benefits:**
    * Direct Admission (No Entrance Exam like NEET/JEE).
    * Low Tuition Fees (Sarkari subsidy ke saath).
    * English Medium study available.
    """)
    if os.path.exists('service 2.jpeg'): st.image('service 2.jpeg', caption="International Exposure")

with c2:
    st.success("""
    **Job & Lifestyle:**
    * Starting Salary: ₹80,000 - ₹1,50,000+.
    * Safe Hostels & Indian Food available.
    * World-class transportation (Metro & Yandex).
    """)
    if os.path.exists('service 4.jpeg'): st.image('service 4.jpeg', caption="High-Tech Environment")

# 3. WE MANAGE EVERYTHING
st.divider()
st.header("🛠️ Humari Services")
cols = st.columns(3)

services = [
    ("service 3.jpeg", "Hostel & Stay", "Aapke pahunchne se pehle hostel ready."),
    ("service 5.jpeg", "Visa Support", "100% Documentation aur Stamping."),
    ("service 6.jpeg", "Airport Pickup", "Russia mein welcome aur hostel tak drop.")
]

for i, col in enumerate(cols):
    with col:
        if os.path.exists(services[i][0]):
            st.image(services[i][0])
        st.subheader(services[i][1])
        st.write(services[i][2])

# 4. STUDENT REGISTRATION FORM
st.divider()
st.header("📝 Register for Free Counseling")
with st.form("student_form"):
    name = st.text_input("Aapka Naam")
    phone = st.text_input("WhatsApp Number")
    interest = st.selectbox("Kaunsa field pasand hai?", ["Medical (MBBS)", "Technical Jobs", "Business/Other"])
    submit = st.form_submit_button("Join Now")
    if submit:
        st.balloons()
        st.success(f"Dhanyawad {name}! Vicky Singh aapse jald hi connect karenge.")

# 5. MD MESSAGE (Using your Lab Photo)
st.divider()
m1, m2 = st.columns([1, 2])
with m1:
    # Using your uploaded lab photo for professional touch
    if os.path.exists('63576.jpg'): 
        st.image('63576.jpg', caption="Vicky Singh - Managing Director")
with m2:
    st.subheader("A Message from Vicky Singh")
    st.write("""
    "Mera maqsad hai ki har Indian student ko Russia ki top universities aur companies tak pahunchaya jaye. 
    Hum sirf visa nahi lagwate, hum Russia mein aapka dusra ghar bankar aapka khayal rakhte hain."
    """)

# 6. FOOTER
st.markdown(f"""
    <div class="footer">
        <h3>Contact Us (24/7 Support)</h3>
        <p>📞 +91 99296 02844 | +91 95720 95975 | 📞 +7 996 409 8229</p>
        <p>📧 rockysingh4405@gmail.com</p>
        <p>© 2026 Horizon Career. Managed by Vicky Singh.</p>
    </div>
    """, unsafe_allow_html=True)
