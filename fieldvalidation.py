from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def validate_name(name):
    if not name or len(name.strip()) < 2:
        return "Name must be at least 2 characters."
    return None

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not email or not re.match(pattern, email):
        return "Invalid email address."
    return None

def validate_password(password):
    if not password or len(password) < 6:
        return "Password must be at least 6 characters."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."
    return None

@app.route('/')
def index():
    return render_template('fieldvalidation.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    password = data.get('password', '')
    errors = {}
    name_error = validate_name(name)
    if name_error:
        errors['name'] = name_error
    email_error = validate_email(email)
    if email_error:
        errors['email'] = email_error
    password_error = validate_password(password)
    if password_error:
        errors['password'] = password_error
    if errors:
        return jsonify({'success': False, 'errors': errors})
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 