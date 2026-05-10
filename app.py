import os
from flask import Flask, send_from_directory, request

app = Flask(__name__)

# Sabhi photos ko load karne ka stylish rasta
@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory('.', filename)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Horizon Career | Rocky Singh</title>
        <style>
            body { background-color: #050505; color: #f0f0f0; font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; padding: 0; }
            .navbar { background: rgba(20, 20, 20, 0.95); padding: 15px; text-align: center; border-bottom: 2px solid #00FF00; position: sticky; top: 0; z-index: 1000; }
            .hero { position: relative; text-align: center; color: white; border-bottom: 4px solid #00FF00; }
            .hero img { width: 100%; height: 450px; object-fit: cover; opacity: 0.6; }
            .hero-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-shadow: 2px 2px 10px black; }
            
            .container { padding: 40px 20px; max-width: 1100px; margin: auto; }
            .quote-box { background: linear-gradient(135deg, #111, #222); padding: 30px; border-radius: 15px; border-left: 10px solid #00FF00; margin-bottom: 40px; font-style: italic; }
            
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
            .card { background: #151515; border-radius: 12px; overflow: hidden; border: 1px solid #333; transition: 0.3s; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
            .card:hover { transform: translateY(-10px); border-color: #00FF00; box-shadow: 0 0 20px rgba(0,255,0,0.3); }
            .card img { width: 100%; height: 220px; object-fit: cover; }
            .card-content { padding: 20px; }
            
            .contact-section { background: #111; padding: 40px; border-radius: 20px; border: 1px dashed #00FF00; margin-top: 50px; text-align: center; }
            .contact-btn { display: inline-block; background: #00FF00; color: black; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; margin: 10px; }
            
            h2 { color: #00FF00; border-bottom: 2px solid #00FF00; display: inline-block; padding-bottom: 5px; }
        </style>
    </head>
    <body>

        <div class="navbar">
            <h1 style="margin:0; letter-spacing:3px; color:#00FF00;">HORIZON CAREER</h1>
        </div>

        <div class="hero">
            <img src="/images/horizon career.jpeg" alt="Banner">
            <div class="hero-text">
                <h1 style="font-size: 3.5em; margin:0;">ROCKY SINGH</h1>
                <p style="font-size: 1.5em; color: #00FF00;">Founder of Horizon Career | MD - Imperial Rice Exim</p>
            </div>
        </div>

        <div class="container">
            
            <div class="quote-box">
                <h2 style="margin-top:0; border:none;">Founder's Message</h2>
                <p style="font-size: 1.3em;">"Agar aap apne sapno ko sach karne, ek behtareen Doctor banne ya ek achhi international job paane ke liye Russia aana chahte hain, toh main Horizon Career ka founder, Rocky Singh, isme aapki puri help karunga. Aapka bhavishya hamari zimmedari hai."</p>
                <p style="text-align:right; font-weight:bold; color:#00FF00;">- Rocky Singh</p>
            </div>

            <h2>Our Expert Services</h2>
            <div class="grid">
                <div class="card">
                    <img src="/images/service 2.jpeg" alt="Education">
                    <div class="card-content">
                        <h3>MBBS in Russia</h3>
                        <p>Duniya ke top medical universities mein admission aur full documentation support.</p>
                    </div>
                </div>
                <div class="card">
                    <img src="/images/service 3.jpeg" alt="Job">
                    <div class="card-content">
                        <h3>Job Placement</h3>
                        <p>Russia aur international markets mein professional job opportunities ke liye sahi rasta.</p>
                    </div>
                </div>
                <div class="card">
                    <img src="/images/service 4.jpeg" alt="Export">
                    <div class="card-content">
                        <h3>Global Trade</h3>
                        <p>Imperial Rice Exim ke saath high-quality Basmati rice ka international export business.</p>
                    </div>
                </div>
            </div>

            <div class="contact-section">
                <h2>Connect With Us</h2>
                <p style="font-size: 1.2em;">Aapke sapno ki udaan ab dur nahi. Aaj hi humse sampark karein!</p>
                <div style="margin-top:20px;">
                    <p>📧 <b>Email:</b> rockysingh4405@gmail.com</p>
                    <p>📞 <b>India:</b> +91 9929602844</p>
                    <p>🇷🇺 <b>Russia:</b> +7 9964098229</p>
                </div>
                <a href="https://wa.me/919929602844" class="contact-btn">WhatsApp India</a>
                <a href="mailto:rockysingh4405@gmail.com" class="contact-btn" style="background:#fff;">Send Email</a>
            </div>

            <div style="text-align:center; margin-top:50px; color:#666; font-style:italic;">
                <p>"The only way to do great work is to love what you do. Success is not just about destination, it's about the journey."</p>
            </div>

        </div>

        <footer style="text-align:center; padding:30px; background:#111; margin-top:50px; color:#555;">
            © 2026 Horizon Career | Designed by Rocky Singh
        </footer>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)