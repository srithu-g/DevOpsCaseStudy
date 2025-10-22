from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "change-me")

# Basic site / resume data (extracted from provided resume)
PROFILE = {
    "name": "Srithu Gaddolla",
    "title": "Full-Stack Developer",
    "location": "Nizamabad, Telangana, India",
    "email": "srithu.gaddolla@gmail.com",
    "phone": "+91 9100863190",
    "linkedin": "https://www.linkedin.com/in/srithu-gaddolla-009919282/",
    "github": "https://github.com/srithu-g",
    "summary": "AI/ML enthusiast and full-stack developer focused on building production-ready ML systems and clean, modern web apps.",
    "education": {
        "degree": "Bachelor of Technology in Information Technology",
        "institute": "G. Narayanamma Institute of Technology and Science",
        "years": "2022 - 2026",
        "cgpa": "9.10"
    },
    "skills": [
        "Python", "Java", "JavaScript", "C", "HTML", "CSS", "R",
        "Angular", "React.js", "Node.js", "Spring MVC", "FastAPI", "Streamlit",
        "LangChain", "MySQL", "PostgreSQL", "MongoDB", "AWS", "Azure", "Jenkins", "Docker"
    ],
    "experiences": [
        {
            "role": "AI/ML Ops Intern",
            "company": "HealthSathi (Remote)",
            "date": "Jun 2025 – Present",
            "highlights": [
                "Developed TB detection system from cough audio using HeAR embeddings.",
                "Trained XGBoost & Random Forest models on 5,000+ samples (98% accuracy).",
                "Reduced model inference time by ~30% for real-time deployment."
            ]
        },
        {
            "role": "AI & Full-Stack Development Intern",
            "company": "Spinabot (Remote)",
            "date": "Aug 2025 – Present",
            "highlights": [
                "Building AI agents to automate marketing/sales workflows using LangChain and Streamlit.",
                "Worked with Java, Spring Boot, React.js and Node.js for automation pipelines."
            ]
        },
        {
            "role": "Mentee - Micron #Master 2.0",
            "company": "Micron Technology (Hyderabad)",
            "date": "Apr 2025 – Jun 2025",
            "highlights": [
                "Built Medicine Inventory Management System using Angular and ASP.NET Core.",
                "Reduced expiry-related wastage by 40% via automated alerts and tracking."
            ]
        }
    ],
    "projects": [
        {
            "title": "Medicine Inventory Management System",
            "desc": "Angular + ASP.NET Core + SQL Server — token-based auth, expiry tracking, reduced manual checks by 40%."
        },
        {
            "title": "Interactive Credit Card Fraud Detection System",
            "desc": "Node.js + MySQL + Chart.js — real-time monitoring with Twilio SMS alerts, model accuracy 96%."
        },
        {
            "title": "Traveler Bag Security Device",
            "desc": "IoT device using ESP8266, accelerometer, fingerprint sensor and GPS with SMS alerts for theft detection."
        }
    ],
    "achievements": [
        "Finalist - NASA Space Apps Challenge 2024 (National Level)"
    ],
    "leadership": [
        "Led Innovation & Incubation Cell at GNITS; coordinated 10+ initiatives & national-level hackathons."
    ]
}

@app.route("/")
def index():
    year = datetime.now().year
    return render_template("index.html", profile=PROFILE, year=year)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    # NOTE: For a production app wire up an email sending service (SendGrid / SES)
    # For this simple portfolio we will flash a message and show result page.
    if not email or not message:
        flash("Please include your email and a message.", "danger")
        return redirect(url_for("index"))

    # Optionally save to a file for demonstration (not recommended for production)
    try:
        with open("contacts.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} | {name} | {email} | {message}\n")
    except Exception:
        # ignore file write errors
        pass

    return render_template("result.html", name=name, email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=os.environ.get("FLASK_DEBUG", "false").lower()=="true")
