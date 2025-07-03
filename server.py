from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = 'buildwithfbs@gmail.com'
EMAIL_PASSWORD = 'YOUR_APP_PASSWORD_HERE'  # Use App Password

@app.route('/send-lead', methods=['POST'])
def send_lead():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    service = data.get('service')

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = f"New Lead from {name}"

    body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Service: {service}
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return jsonify({"message": "Lead sent successfully!"})
    except Exception as e:
        return jsonify({"message": "Error sending lead", "error": str(e)}), 500

if __name__ == '__main__':
    app.run()



