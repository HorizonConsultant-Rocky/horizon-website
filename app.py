from flask import Flask
import os

app = Flask(__name__)

# --- WEBSITE CONTENT ---
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Horizon Career | Study in Russia</title>
        <style>
            :root { --primary: #2c3e50; --secondary: #3498db; --accent: #e74c3c; --light: #ecf0f1; }
            body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; color: #333; line-height: 1.6; background: var(--light); }
            
            /* Header & Nav */
            header { background: var(--primary); color: white; padding: 20px 0; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            nav { background: #34495e; padding: 10px; text-align: center; position: sticky; top: 0; }
            nav a { color: white; text-decoration: none; margin: 0 15px; font-weight: bold; font-size: 14px; }
            nav a:hover { color: var(--secondary); }

            /* Hero Section */
            .hero { background: linear-gradient(rgba(44, 62, 80, 0.8), rgba(44, 62, 80, 0.8)), url('https://images.unsplash.com/photo-1513530534585-c7b1394c6d51?auto=format&fit=crop&w=1350&q=80'); 
                    background-size: cover; color: white; padding: 100px 20px; text-align: center; }
            .hero h1 { font-size: 3rem; margin: 0; }
            .hero p { font-size: 1.2rem; max-width: 800px; margin: 20px auto; }

            /* Container */
            .container { max-width: 1100px; margin: auto; padding: 20px; overflow: hidden; }

            /* Section Styling */
            section { padding: 40px 0; border-bottom: 1px solid #ddd; }
            .section-title { text-align: center; color: var(--primary); margin-bottom: 40px; }

            /* Details / Grid */
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: 0.3s; }
            .card:hover { transform: translateY(-5px); }
            .card h3 { color: var(--secondary); border-bottom: 2px solid var(--secondary); display: inline-block; padding-bottom: 5px; }

            /* Footer */
            footer { background: var(--primary); color: white; text-align: center; padding: 40px 20px; margin-top: 40px; }
            .footer-links { margin-bottom: 20px; }
            .footer-links a { color: #bdc3c7; text-decoration: none; margin: 0 10px; font-size: 13px; }
            .designer { color: var(--secondary); font-weight: bold; font-size: 1.1rem; }

            /* Responsive */
            @media (max-width: 768px) { .hero h1 { font-size: 2rem; } }
        </style>
    </head>
    <body>

        <header>
            <h1>HORIZON CAREER</h1>
            <p>Your Gateway to Education in Russia</p>
        </header>

        <nav>
            <a href="#">HOME</a>
            <a href="#about">ABOUT US</a>
            <a href="#services">SERVICES</a>
            <a href="#contact">CONTACT</a>
        </nav>

        <div class="hero">
            <h1>Build Your Future in Russia</h1>
            <p>We provide end-to-end consultancy for Indian students seeking top-tier MBBS, Engineering, and Technical education in world-class Russian Universities.</p>
        </div>

        <div class="container">
            <section id="about">
                <h2 class="section-title">About Horizon Career</h2>
                <p>Horizon Career is a premier consultancy firm dedicated to bridging the gap between Indian aspirations and Russian excellence. We understand the challenges of studying abroad, and we are here to simplify every step—from university selection to visa processing.</p>
            </section>

            <section id="services">
                <h2 class="section-title">Our Detailed Services</h2>
                <div class="grid">
                    <div class="card">
                        <h3>University Selection</h3>
                        <p>We analyze your profile and suggest the best government-recognized universities in Moscow, Saint Petersburg, and Kazan.</p>
                    </div>
                    <div class="card">
                        <h3>Admission Support</h3>
                        <p>Complete documentation, invitation letter processing, and application tracking for a 100% success rate.</p>
                    </div>
                    <div class="card">
                        <h3>Visa & Travel</h3>
                        <p>Full assistance with student visa documentation, flight bookings, and pre-departure briefings.</p>
                    </div>
                    <div class="card">
                        <h3>Local Assistance</h3>
                        <p>Support in Russia for hostel accommodation, local sim cards, and bank account opening.</p>
                    </div>
                </div>
            </section>

            <section id="details">
                <h2 class="section-title">Why Russia?</h2>
                <ul style="list-style-type: square; columns: 2; padding: 20px;">
                    <li>Globally Recognized Degrees</li>
                    <li>Low Tuition Fees (Subsidized)</li>
                    <li>No Entrance Exams like IELTS/TOEFL</li>
                    <li>Modern Infrastructure & Labs</li>
                    <li>European Standard of Living</li>
                    <li>High Safety for International Students</li>
                    <li>English Medium Courses Available</li>
                    <li>Direct Admission Process</li>
                </ul>
            </section>
        </div>

        <footer>
            <div class="footer-links">
                <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">FAQ</a>
            </div>
            <p>© 2026 <b>Horizon Career Consultancy</b>. All Rights Reserved.</p>
