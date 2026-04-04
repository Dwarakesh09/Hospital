from datetime import datetime
from flask import Flask, render_template, request
import os
import csv

app = Flask(__name__)

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

        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        day = datetime.now().strftime("%A")

        # ✅ CSV Saving
        file_exists = os.path.isfile('submitted_data.csv')

        with open('submitted_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(['Name', 'Age', 'Issue', 'Email', 'Phone', 'Gender', 'Date', 'Day'])

            writer.writerow([name, age, issue, email, phone, gender, date, day])

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

if __name__ == '__main__':
    app.run(debug=True)
