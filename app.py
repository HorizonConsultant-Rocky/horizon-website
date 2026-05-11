import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Horizon Career | Russia Employment & Education Expert", layout="wide")

# Custom CSS for High-End Design
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { background-color: #f4f7f9; }
    .hero-container { background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%); padding: 60px; border-radius: 0 0 50px 50px; color: white; text-align: center; margin-bottom: 40px; }
    .info-card { background: white; padding: 25px; border-radius: 15px; border-left: 8px solid #1a73e8; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .stat-box { text-align: center; padding: 20px; background: #e3f2fd; border-radius: 10px; border: 1px solid #bbdefb; }
    .stat-number { font-size: 30px; font-weight: bold; color: #1565c0; }
    .step-box { padding: 15px; border-radius: 50%; background: #1a73e8; color: white; width: 40px; height: 40px; display: inline-block; text-align: center; line-height: 10px; font-weight: bold; }
    .footer { background: #121212; color: white; padding: 50px; border-radius: 20px 20px 0 0; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 1. MEGA HERO SECTION
st.markdown("""
    <div class="hero-container">
        <h1>HORIZON CAREER: YOUR GATEWAY TO RUSSIA</h1>
        <p style="font-size: 22px;">India's Most Trusted Career Consultancy for Russian Opportunities</p>
        <p>Managed by <b>Vicky Singh</b> | Trusted by Students Across India</p>
    </div>
    """, unsafe_allow_html=True)

if os.path.exists('horizon career.jpeg'):
    st.image('horizon career.jpeg', use_container_width=True)

# 2. QUICK STATS (Motivation & Facts)
st.markdown("### 📊 Quick Facts: Russia 2026")
s1, s2, s3, s4 = st.columns(4)
with s1: st.markdown('<div class="stat-box"><p class="stat-number">100%</p><p>Visa Success</p></div>', unsafe_allow_html=True)
with s2: st.markdown('<div class="stat-box"><p class="stat-number">₹80k+</p><p>Avg. Starting Salary</p></div>', unsafe_allow_html=True)
with s3: st.markdown('<div class="stat-box"><p class="stat-number">30k+</p><p>Indian Students</p></div>', unsafe_allow_html=True)
with s4: st.markdown('<div class="stat-box"><p class="stat-number">24/7</p><p>Local Support</p></div>', unsafe_allow_html=True)

# 3. DETAILED COMPARISON (India vs Russia)
st.divider()
st.header("🔍 India vs Russia: Career Comparison")
col_inv1, col_inv2 = st.columns(2)

with col_inv1:
    st.markdown("""
    <div class="info-card">
        <h4>🇮🇳 Career in India</h4>
        <ul>
            <li>High competition in entrance exams (NEET/JEE).</li>
            <li>Limited seats in government colleges.</li>
            <li>High cost of private education (₹60L - ₹1Cr+).</li>
            <li>Stagnant starting salaries in many sectors.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_inv2:
    st.markdown("""
    <div class="info-card" style="border-left-color: #2e7d32;">
        <h4>🇷🇺 Career in Russia</h4>
        <ul>
            <li>Direct admission in Top-tier Universities.</li>
            <li>Subsidized tuition fees (Government funded).</li>
            <li>International Exposure & Global Degree.</li>
            <li>Easier pathway to European & Western markets.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 4. STEP-BY-STEP PROCESS (The Horizon Journey)
st.header("🛠️ Humara Process: Form Se Flight Tak")
st.write("Hum aapka haath tab tak nahi chhodte jab tak aap settle nahi ho jaate.")

steps = [
    ("Counseling", "Aapki profile analyze karke sahi career path chunna."),
    ("Document Prep", "Apostille, Translation aur Medical Insurance ka kaam."),
    ("Visa Stamping", "Embassy se visa lagwane ki poori zimmedari hamari."),
    ("Pre-Departure", "Russia ki lifestyle aur rules ke baare mein briefing."),
    ("On-Arrival", "Airport pickup, Sim card, aur Hostel check-in.")
]

for i, (title, desc) in enumerate(steps, 1):
    st.markdown(f"**Step {i}: {title}** - {desc}")

# 5. MEGA INFO SECTION: LIFE IN RUSSIA
st.divider()
st.header("🌍 Russia Mein Zindagi Kaisi Hogi?")
tab1, tab2, tab3 = st.tabs(["🏠 Accommodation", "🍲 Food & Expenses", "🚆 Connectivity"])

with tab1:
    st.write("""
    - **University Hostels:** Ekdum safe, centralized heating ke saath.
    - **Rentals:** Sheron mein flats ka option bhi available hai (Hum dhoondne mein help karenge).
    - **Security:** CCTV aur 24/7 guard security har student hostel mein hoti hai.
    """)
    if os.path.exists('service 3.jpeg'): st.image('service 3.jpeg', width=400)

with tab2:
    st.write("""
    - **Monthly Living Cost:** ₹15,000 se ₹25,000 ke beech (Shehar ke hisaab se).
    - **Indian Mess:** Zyada tar badi universities mein Indian khana available hai.
    - **Part-time Work:** Students ke liye kaam karne ke kanooni mauke.
    """)

with tab3:
    st.write("""
    - **Yandex Go:** Russia ki sabse best taxi service.
    - **Metro Rail:** Moscow aur St. Petersburg mein world-class transport.
    - **Direct Flights:** Delhi aur Mumbai se Moscow ke liye direct connectivity.
    """)

# 6. MOTIVATIONAL QUOTE
st.markdown("""
    <div style="background: #fff3e0; padding: 40px; border-radius: 20px; text-align: center; border: 1px dashed #ff9800; margin: 40px 0;">
        <h2 style="color: #e65100;">"Waqt aur Mauka intezaar nahi karte."</h2>
        <p>Aaj liya gaya ek sahi faisla aapka aur aapki family ka future badal sakta hai. 
        Horizon Career aapke har kadam par saath hai.</p>
    </div>
    """, unsafe_allow_html=True)

# 7. FOOTER & CONTACTS
st.markdown(f"""
    <div class="footer">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <h3>HORIZON CAREER</h3>
                <p>Leading Career Consultancy for Russia & Beyond.</p>
                <p><b>MD: Vicky Singh</b></p>
            </div>
            <div style="flex: 1; min-width: 300px;">
                <h4>Emergency Helpdesk</h4>
                <p>📞 India: +91 99296 02844 | +91 95720 95975</p>
                <p>📞 Russia: +7 996 409 8229</p>
                <p>📧 Email: rockysingh4405@gmail.com</p>
            </div>
        </div>
        <hr style="border-color: #333;">
        <p style="text-align: center; font-size: 14px; opacity: 0.6;">
            © 2026 Horizon Career. All Rights Reserved. Managed with dedication by Vicky Singh.
        </p>
    </div>
    """, unsafe_allow_html=True)
