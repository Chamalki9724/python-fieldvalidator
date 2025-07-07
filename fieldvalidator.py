# form_validator.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

def validate_email(email):
    return "@" in email and "." in email

def validate_password(pwd):
    return len(pwd) >= 6

form_data = [
    {"email": "user1@test.com", "password": "secret"},
    {"email": "bademail.com", "password": "123"},
    {"email": "qa@domain.org", "password": "testing123"},
]

for entry in form_data:
    email_ok = validate_email(entry["email"])
    pwd_ok = validate_password(entry["password"])
    print(f"Email: {entry['email']} → {'OK' if email_ok else 'INVALID'}")
    print(f"Password: {'OK' if pwd_ok else 'TOO SHORT'}\n")
