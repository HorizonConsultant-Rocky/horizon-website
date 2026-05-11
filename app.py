import streamlit as st
import os

# 1. Basic Page Configuration
st.set_page_config(page_title="Horizon Career | Russia Expert", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .hero { background-color: #1a73e8; color: white; padding: 50px; text-align: center; border-radius: 20px; margin-bottom: 30px; }
    .contact-box { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #1a73e8; }
    </style>
    """, unsafe_allow_html=True)

# 2. Safety Function for Images
def display_img(file_name, caption):
    # Check if file exists to prevent crash
    if os.path.exists(file_name):
        st.image(file_name, caption=caption, use_container_width=True)
    else:
        # If file is missing, show a note instead of crashing the site
        st.info(f"📸 Image '{file_name}' setup ho rahi hai...")

# --- WEBSITE CONTENT START ---

# Header Section
st.markdown('<div class="hero"><h1>HORIZON CAREER</h1><p>Managed by Vicky Singh - Russia Career Experts</p></div>', unsafe_allow_html=True)

# Main Banner
display_img('horizon career.jpeg', "Horizon Career Office")

# Information Columns
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.header("🇷🇺 Why Russia?")
    st.write("""
    - **No Entrance Exams:** Direct admission in top universities.
    - **Affordable Fees:** Low tuition costs with high-quality education.
    - **High Salary:** Starting packages from ₹80,000 to ₹1.5 Lakhs.
    """)
    display_img('service 2.jpeg', "Educational Excellence")

with col2:
    st.header("📞 Contact Details")
    st.markdown("""
    <div class="contact-box">
        <p><b>India (Vicky Singh):</b><br>+91 99296 02844 | +91 95720 95975</p>
        <p><b>Russia Helpline:</b><br>+7 996 409 8229</p>
        <p><b>Email:</b> rockysingh4405@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)
    display_img('service 4.jpeg', "Support System")

# Services Section
st.divider()
st.header("🛠️ Our Services")
s1, s2, s3 = st.columns(3)

with s1:
    display_img('service 3.jpeg', "Accommodation")
    st.write("Hostel aur Flat ki suvidha.")
with s2:
    display_img('service 5.jpeg', "Visa Support")
    st.write("100% Visa assistance.")
with s3:
    display_img('service 6.jpeg', "Arrival Support")
    st.write("Airport pickup aur local help.")

# Registration Form
st.divider()
st.header("📝 Register Now")
with st.form("registration_form"):
    u_name = st.text_input("Aapka Naam")
    u_whatsapp = st.text_input("WhatsApp Number")
    u_interest = st.selectbox("Kaunse field mein interest hai?", ["Medical", "Technical", "Business", "Other"])
    
    submitted = st.form_submit_button("Submit Details")
    if submitted:
        if u_name and u_whatsapp:
            st.success(f"Dhanyawad {u_name}! Hum aapse jald connect karenge.")
        else:
            st.error("Please saari details bharein.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; opacity: 0.7;'>© 2026 Horizon Career. Managed by Vicky Singh.</p>", unsafe_allow_html=True)
