from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Aapka GitHub username aur repo name yahan hai
    base_url = "https://raw.githubusercontent.com/HorizonConsultant-Rocky/horizon-website/main/"
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Horizon Career | Study in Russia</title>
        <style>
            body {{ font-family: 'Poppins', sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; color: #333; }}
            header {{ 
                background: linear-gradient(rgba(0,0,50,0.8), rgba(0,0,50,0.8)), 
                            url('{base_url}horizon%20career.jpeg'); 
                background-size: cover; background-position: center;
                color: white; padding: 100px 20px; text-align: center;
            }}
            .container {{ max-width: 1200px; margin: auto; padding: 40px 20px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; }}
            .card {{ background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.1); text-align: center; transition: 0.3s; }}
            .card:hover {{ transform: translateY(-10px); }}
            .card img {{ width: 100%; height: 250px; object-fit: cover; border-bottom: 4px solid #d32f2f; }}
            .card-content {{ padding: 20px; }}
            .btn {{ 
                display: inline-block; background: #25d366; color: white; padding: 15px 30px; 
                text-decoration: none; border-radius: 30px; font-weight: bold; margin: 10px; font-size: 1.1rem;
            }}
            .email-btn {{ background: #d32f2f; }}
            footer {{ background: #1a1a1a; color: white; text-align: center; padding: 30px; margin-top: 50px; }}
            h1 {{ font-size: 3rem; margin-bottom: 10px; text-transform: uppercase; }}
            .contact-section {{ background: white; padding: 40px; border-radius: 20px; text-align: center; margin-top: 40px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
        </style>
    </head>
    <body>
        <header>
            <h1>HORIZON CAREER CONSULTANCY</h1>
            <p>Your Trusted Gateway to Education in Russia</p>
        </header>

        <div class="container">
            <h2 style="text-align:center; margin-bottom:40px; font-size: 2rem; color: #2c3e50;">Our Premium Services</h2>
            <div class="grid">
                <div class="card">
                    <img src="{base_url}service%202.jpeg" alt="Admission">
                    <div class="card-content"><h3>Direct Admission</h3><p>Fast track process for Russian Universities.</p></div>
                </div>
                <div class="card">
                    <img src="{base_url}service%203.jpeg" alt="Visa">
                    <div class="card-content"><h3>Visa Assistance</h3><p>Guaranteed visa support and documentation.</p></div>
                </div>
                <div class="card">
                    <img src="{base_url}service%204.jpeg" alt="Support">
                    <div class="card-content"><h3>Local Support</h3><p>Hostel and SIM card assistance in Russia.</p></div>
                </div>
            </div>

            <div class="contact-section">
                <h2 style="color: #2c3e50;">Contact MD Rocky Singh</h2>
                <p>Ready to start your journey? Get in touch today.</p>
                <a href="https://wa.me/919929602844" class="btn">WhatsApp India</a>
                <a href="https://wa.me/79964098229" class="btn">WhatsApp Russia</a>
                <br>
                <a href="mailto:rockysingh4405@gmail.com" class="btn email-btn">Email Us: rockysingh4405@gmail.com</a>
            </div>
        </div>

        <footer>
            <p>&copy; 2026 Horizon Career Consultancy | Designed and Managed by <b>Rocky Singh</b></p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
