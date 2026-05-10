from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizon Career | Study in Russia</title>
    <style>
        :root { --primary: #2c3e50; --secondary: #3498db; --light: #ecf0f1; }
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: var(--light); color: #333; }
        header { background: var(--primary); color: white; padding: 40px 20px; text-align: center; }
        .container { max-width: 1000px; margin: 20px auto; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { margin: 0; font-size: 2.5rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; }
        .card { padding: 20px; border-left: 5px solid var(--secondary); background: #f9f9f9; }
        footer { text-align: center; padding: 30px; margin-top: 40px; background: #2c3e50; color: white; }
        .designer { color: #3498db; font-weight: bold; }
    </style>
</head>
<body>
    <header>
        <h1>HORIZON CAREER</h1>
        <p>Expert Consultancy for Education in Russia</p>
    </header>
    <div class="container">
        <h2>Why Choose Russia for Your Career?</h2>
        <p>Russia offers world-class education at affordable costs. Whether it's MBBS or Engineering, we help you get direct admission in top universities.</p>
        <div class="grid">
            <div class="card"><h3>Top Universities</h3><p>Direct admission in Moscow and Saint Petersburg.</p></div>
            <div class="card"><h3>Low Tuition Fees</h3><p>Quality education that fits your budget.</p></div>
            <div class="card"><h3>Visa Support</h3><p>100% assistance with documentation and travel.</p></div>
        </div>
    </div>
    <footer>
        <p>© 2026 Horizon Career | Designed and Developed by <span class="designer">Rocky Singh</span></p>
    </footer>
</body>
</html>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
