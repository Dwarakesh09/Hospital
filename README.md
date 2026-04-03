#  Hospital Management System

## 📌 Project Overview
This Hospital Management System is a web-based application designed to streamline and automate basic hospital operations. It helps in managing patient details, recording medical issues, and maintaining organized records, improving efficiency and reducing manual work.

---

##  Features

-  Patient Registration: Collect patient details through a simple form  
-  Record Management: Store patient data including issue, age, and contact details  
-  Date & Time Tracking: Automatically records submission date and day  
-  Data Display: Displays submitted details on a separate page  
-  Data Storage: Saves records in a text file (can be upgraded to database)  
-  Form Reset: Clear input fields instantly  

---

##  Technology Stack

- **Frontend:** HTML5, CSS3  
- **Backend:** Python (Flask)  
- **Database:** File-based storage (`.txt`) *(can be upgraded to SQLite/MongoDB)*  
- **Hosting:** Render / AWS / Heroku *(optional deployment)*  

---

##  Project Structure

```
Hospital/
│
├── app.py
├── submitted_data.txt
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── details.html
│
├── static/
│   └── style.css
```

---

##  Installation & Setup

### 1️ Clone the repository
```bash
git clone https://github.com/Dwarakesh09/Hospital.git
cd Hospital
```

### 2️ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️ Run the application
```bash
python app.py
```

### 4️ Open in browser
```
http://127.0.0.1:5000/
```

---

##  Usage

- Fill in patient details using the form  
- Submit the form to view entered data  
- Data is saved automatically in `submitted_data.txt`  
- Extend the system to view all submissions or manage records  

---

##  Future Enhancements

-  Integrate database (SQLite / MongoDB)  
-  View all patient records in table format  
-  Search and filter patient data  
-  Delete or update records  
-  Deploy application online  
-  Add authentication (admin login system)  

---

##  Contribution Guidelines

1. Fork the repository  
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to GitHub:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a Pull Request  

---

##  Author

**Dwarakesh Raghu**  
 1234dwarakesh@gmail.com  

---

##  License

This project is open-source and free to use.
