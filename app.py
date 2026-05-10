from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Horizon Career | Study in Russia</title>
        <style>
            body { font-family: 'Arial', sans-serif; margin: 0; padding: 0; background-color: #f4f7f6; }
            header { background: #2c3e50; color: white; padding: 50px 20px; text-align: center; }
            .container { max-width: 1100px; margin: auto; padding: 20px; }
            .section-title { text-align: center; color: #2c3e50; margin-bottom: 40px; font-size: 32px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-top: 5px solid #3498db; }
            .card h3 { color: #3498db; margin-top: 0; }
            footer { background: #2c3e50; color: white; text-align: center; padding: 20px; margin-top: 50px; }
            .highlight { color: #3498db; font-weight: bold; }
        </style>
    </head>
    <body>
        <header>
            <h1>HORIZON CAREER CONSULTANCY</h1>
            <p>Your Trusted Gateway to Top Russian Universities</p>
        </header>
        
        <div class="container">
            <h2 class="section-title">Why Choose Russia?</h2>
            <div class="grid">
                <div class="card">
                    <h3>Globally Recognized Degrees</h3>
                    <p>Get degrees that are valued worldwide and recognized by major international bodies.</p>
                </div>
                <div class="card">
                    <h3>Low Tuition Fees</h3>
                    <p>Russian education is highly subsidized, making it affordable for Indian students.</p>
                </div>
                <div class="card">
                    <h3>Direct Admission</h3>
                    <p>No entrance exams like IELTS or TOEFL required. Smooth and direct process.</p>
                </div>
                <div class="card">
                    <h3>Local Assistance</h3>
                    <p>Support in Russia for hostel accommodation, local SIM cards, and registration.</p>
                </div>
            </div>
        </div>

        <footer>
            <p>&copy; 2026 <b>Horizon Career Consultancy</b>. All Rights Reserved.</p>
            <p>Designed and Managed by <span class="highlight">Rocky Singh</span></p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
