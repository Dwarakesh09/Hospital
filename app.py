from datetime import datetime
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# ✅ Home route (IMPORTANT)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def details():
    if 'name' in request.form:
        name = request.form['name']
        age = request.form['age']
        issue = request.form.get('issue', '')
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form.get('gender') or 'Not Provided'

        # ✅ Date & Day
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        day = datetime.now().strftime("%A")

        submitted_data = {
            'name': name,
            'age': age,
            'issue': issue,
            'email': email,
            'phone': phone,
            'gender': gender,
            'date': date,
            'day': day
        }

        # ✅ Save data
        with open('submitted_data.txt', 'a') as f:
            f.write(str(submitted_data) + '\n')

        return render_template(
            'details.html',
            name=name,
            age=age,
            issue=issue,
            email=email,
            phone=phone,
            gender=gender,
            date=date,
            day=day
        )
    else:
        return "Name is required!", 400


# ✅ Run app (IMPORTANT)
if __name__ == '__main__':
    app.run(debug=True)